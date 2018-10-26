from django.contrib import admin
from .models import Usuario
from .models import Captura
from .models import Rostro

admin.site.register(Usuario)
admin.site.register(Captura)
admin.site.register(Rostro)