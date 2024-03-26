from django.shortcuts import render,HttpResponse,redirect
from .models import redesSociales, IconRedesSociales


# Create your views here.

def home(request):
    redes = redesSociales.objects.all()
    curIcon = {red.redSocial: red.redSocial.icon for red in redes}  # Crear un diccionario de red social: ícono
    return render(request, 'core/home.html', {'curRedes': redes, 'curIcon': curIcon})

def about(request):
    return render(request,'core/about.html')
def contacto(request):
    return render(request,'core/contacto.html')
