from django.contrib import admin
from .models import Page

# Register your models here.
admin.site.register(Page)

title = "Administración Dorita"

subtitle = "Panel de gestión"

# Configuracion del panel

admin.site.site_header = title
admin.site.site_title = title

admin.site.index_title = subtitle