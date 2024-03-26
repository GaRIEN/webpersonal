from django.db import models

# Create your models here.
class IconRedesSociales(models.Model):
    nombre=models.CharField(max_length=50, verbose_name='red social')
    icon=models.ImageField(upload_to='icons_redes_sociales',null=False, blank=False)

    def __str__(self):
        return self.nombre
    
class redesSociales(models.Model):
    redSocial=models.ForeignKey(IconRedesSociales, on_delete=models.PROTECT ,verbose_name='red social')
    link=models.URLField(blank=True, null=True)
    activo=models.BooleanField(default=True);
    
    def __str__(self):
        return str(self.redSocial)
    