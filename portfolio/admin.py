from django.contrib import admin
from .models import Project

# Register your models here.
class portafolioAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')

admin.site.register(Project,portafolioAdmin)
