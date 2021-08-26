FROM python:3.8-slim

WORKDIR /gen

COPY . /gen

RUN pip3 install -r requirements.txt

RUN pip3 install Tortoise-ORM
RUN pip3 install fastapi_offline

EXPOSE 8000

VOLUME [ "/gen" ]

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]
