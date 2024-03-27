from django.shortcuts import render
# from .models import redesSociales, IconRedesSociales

# def home(request):
#     # redes = redesSociales.objects.all()
            
#     return render(request, 'core/home.html', {'curRedes': redes})


def home(request):
       
   return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contacto(request):
    return render(request, 'core/contacto.html')

