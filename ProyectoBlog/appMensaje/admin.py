from django.contrib import admin
from .models import Emisor, Mensaje, Receptor
# Register your models here.

admin.site.register(Mensaje)
admin.site.register(Emisor)
admin.site.register(Receptor)
