from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Documento)
admin.site.register(Historico)

admin.site.register(AnexoI)
admin.site.register(AnexoII)
admin.site.register(AnexoIII)
admin.site.register(AnexoIV)

admin.site.register(InfoGerais)
