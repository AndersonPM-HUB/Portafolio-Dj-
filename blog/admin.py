from django.contrib import admin
from .models import Post

# modificar el admin 

@admin.register(Post)
class PostAdmin(admin.ModelAdmin): 
    list_display=('title', 'image','fecha')