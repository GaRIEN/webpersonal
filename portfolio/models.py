from django.db import models

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=200, verbose_name='titulo')
    description=models.TextField(verbose_name='descripcion')
    image=models.ImageField(upload_to='projects',verbose_name='imagen')
    link=models.URLField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name='fecha creacion')
    update=models.DateTimeField(auto_now=True, verbose_name='fecha modificacion')

    def __str__(self) :
        return f'{self.title}'
    
    class Meta:
        verbose_name='proyecto'
        verbose_name_plural='proyectos'
        ordering=['-created']