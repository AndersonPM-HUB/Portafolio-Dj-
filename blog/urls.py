from django.urls import path
from . import views


urlpatterns=[ 
    path('', views.post, name='listado de post'),
    path('<int:post_id>', views.post_detail,  name='post')
]