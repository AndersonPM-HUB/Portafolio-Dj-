from distutils.command.upload import upload
from email import contentmanager
from email.mime import image
from django.db import models
from django.db.models import CharField
from ckeditor.fields import RichTextField

import datetime



# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=100)
    content = RichTextField()
    image= models.ImageField(upload_to='blog/images')
    fecha = models.DateTimeField(auto_now_add=True)