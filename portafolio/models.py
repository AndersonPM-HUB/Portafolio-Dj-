from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models.fields import URLField
from ckeditor.fields import RichTextField


# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    description = RichTextField()
    image = ImageField(upload_to="portafolio/images/")
    url = URLField(blank=True)
