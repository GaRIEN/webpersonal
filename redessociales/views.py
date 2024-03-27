
from django.shortcuts import render
from .models import IconRedesSociales, redesSociales


def redes(request):
    redes = redesSociales.objects.all()
    # Pasar los datos al contexto de renderizado
    return render(request, 'core/base.html', {'curRedes': redes})
