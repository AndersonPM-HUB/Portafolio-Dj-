from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models.fields import URLField


# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=200)
    image = ImageField(upload_to="portafolio/images/")
    url = URLField(blank=True)
