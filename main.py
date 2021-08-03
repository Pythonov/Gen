from fastapi_offline import FastAPIOffline
from src.models.models import *
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise, models
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel, ValidationError


app = FastAPIOffline()


register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["src.models.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

# Early-init

Tortoise.init_models(["src.models.models"], "models")
query_pydantic = pydantic_model_creator(
    BaseForQueries, name="BaseForQueries", exclude_readonly=True
)


class SeparatorPyd(BaseModel):
    target_class: str
    data: dict


def parse_args(input_JSON: dict):
    try:
        input_data = SeparatorPyd.parse_obj(input_JSON)
        data = input_data.data
        target_calss = input_data.target_class
    except ValidationError as e:
        target_calss = "Wrong data, motherfucker!"
        data = e

    return target_calss, data


"""
target_class - ["genes","people"]

Request for "genes":
    "target_class": "genes",
    "data": {
        "gene_code": "Ген садовода",
        "comment": "Тот самый ген",
        "rs_code": "1",
        "poly_type": "ультра полезный",
        "poly_status": "---",
        "interpretation": "+5 к владению тяпкой"
    }

Data for "people"
    "target_class": "people",
    "data": {
        "lab_number": "1",
        "name": "ГЕНнадий Садовод",
        "sex": "Овощ",
        "date_of_birth": "01.01.1980",
        "material_type": "Удобрение",
        "date_of_analysis": "+5 к владению тяпкой",
        "reason_of_analysis": "непреодолимая тяга к картохе",
        "comment": "и кукурузице"
    }
"""


@app.post(f"/add")
async def post(cp: query_pydantic):
    target_class, data = parse_args(cp.dict())
    objIn_pydantic = pydantic_model_creator(
        models_dict[target_class],
        name=target_class,
        exclude_readonly=True,
    )
    obj_created = objIn_pydantic.parse_obj(data)
    obj = await models_dict[target_class].create(**obj_created.dict(exclude_unset=True))
    response = await objIn_pydantic.from_tortoise_orm(obj)
    return {"status": "Ok", "data": response}


@app.post("/tie")
async def tie(gen_id: int, pers_id: int):
    objIn_pydantic = pydantic_model_creator(
        models_dict["people_genes"],
        name="People_genes",
        exclude_readonly=True,
    )
    data = {"genes_id": gen_id, "people_id": pers_id}
    obj_created = objIn_pydantic.parse_obj(data)
    obj = await models_dict["people_genes"].create(
        **obj_created.dict(exclude_unset=True)
    )
    response = await objIn_pydantic.from_tortoise_orm(obj)
    return {"status": "Ok", "data": response}


@app.post("/tie_many")
async def tie_many(pers_id: int, genes: list):
    objIn_pydantic = pydantic_model_creator(
        models_dict["people_genes"],
        name="People_genes",
        exclude_readonly=True,
    )
    for gen in genes:
        data = {"genes_id": gen, "people_id": pers_id}
        obj_created = objIn_pydantic.parse_obj(data)
        obj = await models_dict["people_genes"].create(
            **obj_created.dict(exclude_unset=True)
        )
    response = await objIn_pydantic.from_tortoise_orm(obj)
    return {"status": "Ok", "data": response}


@app.post(f"/get_all")
async def get_all(cp: query_pydantic):
    target_class, data = parse_args(cp.dict())
    obj_pydantic = pydantic_model_creator(
        models_dict[target_class], name=target_class, exclude=("people_geness",)
    )
    response = await obj_pydantic.from_queryset(models_dict[target_class].all())
    return {"status": "Ok", "data": response}


@app.post(f"/get")
async def get(cp: query_pydantic):
    target_class, data = parse_args(cp.dict())
    obj_pydantic = pydantic_model_creator(
        models_dict[target_class], name=target_class, exclude=("people_geness",)
    )
    response = await obj_pydantic.from_queryset_single(
        models_dict[target_class].get(**data)
    )
    return {"status": "Ok", "data": response}
