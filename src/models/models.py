"""

You have to register all new models
in models_dict in format
{'name_for_json': name of class}

"""

from tortoise import models, fields


class BaseForQueries(models.Model):
    target_class = fields.CharField(max_length=100)
    data = fields.JSONField()


class PeoplesGenes(models.Model):
    people = fields.ForeignKeyField("models.People")
    genes = fields.ForeignKeyField("models.Genes")

    class Meta:
        table = "people_genes"


class Genes(models.Model):
    id = fields.IntField(pk=True)
    gene_code = fields.CharField(max_length=50, unique=False)
    comment = fields.TextField()
    rs_code = fields.CharField(max_length=25, unique=False)
    poly_type = fields.CharField(max_length=50, unique=False)
    poly_status = fields.CharField(max_length=50, unique=False)
    interpretation = fields.TextField()

    def __str__(self):
        return self.gene_code

    class Meta:
        ordering = ["gene_code"]


class People(models.Model):
    id = fields.IntField(pk=True)
    lab_number = fields.CharField(max_length=10, unique=True)
    name = fields.CharField(max_length=50, unique=False)
    sex = fields.CharField(max_length=10, unique=False)
    date_of_birth = fields.CharField(max_length=20, unique=False)
    material_type = fields.CharField(max_length=50, unique=False)
    date_of_analysis = fields.CharField(max_length=50, unique=False)
    reason_of_analysis = fields.TextField()
    comment = fields.TextField(null=True)
    genes: fields.ManyToManyRelation["Genes"] = fields.ManyToManyField("models.Genes")

    def __str__(self):
        return self.id

    class Meta:
        ordering = ["date_of_analysis"]


models_dict = {
    "people": People,
    "genes": Genes,
    "people_genes": PeoplesGenes,
}
