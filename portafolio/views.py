from django.shortcuts import render
from .models import Project


# Create your views here.
def verPortafolio(request):
    # traer todos los objetos 
    proyectos= Project.objects.all()

    return render(request,'index.html',{'proyectos': proyectos})