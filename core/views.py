from django.shortcuts import render
from .models import redesSociales, IconRedesSociales

def home(request):
    redes = redesSociales.objects.all()
    
    # Iterar sobre cada red social y buscar su imagen correspondiente en IconRedesSociales
    for red in redes:
        try:
            # Buscar la imagen correspondiente en IconRedesSociales basada en el nombre de la red social
            icono = IconRedesSociales.objects.get(nombre=red.redSocial)
            # Asignar la imagen encontrada a la red social actual
            red.imagen = icono.icon
        except IconRedesSociales.DoesNotExist:
            # Si no se encuentra una imagen, asignar None
            red.imagen = None
    
    return render(request, 'core/home.html', {'curRedes': redes})

def about(request):
    return render(request, 'core/about.html')

def contacto(request):
    return render(request, 'core/contacto.html')

