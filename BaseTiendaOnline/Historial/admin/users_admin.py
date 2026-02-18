from django.contrib import admin

from Historial.models import Usuarios



class UserAdmin(admin.ModelAdmin):
    list_display = ('nombre','email','telefono','nie','nc','rol','fecha_nacimiento','edad','actualizado') # Esto es las columnas en mi panel de administración
    list_filter = ('nombre','edad')
    search_fields = ('email','nombre','nie')
    # añadir un campo editable
    list_editable = ('telefono','email','edad')
    # añade páginas con un límite de campos a mostrar
    list_per_page = 15

    fieldsets = (
    ("Informacion",{'fields':('nombre','email','telefono','nie','nc','fecha_nacimiento','edad')}),
    ("Configuracion", {'fields': ('password','rol',)})
    )

    add_fieldsets = (
    ("Informacion Personal",{'fields':('nombre','email','edad'),
                    'classes':('wide',)}),
    ("Informacion de iniciar sesion",
     {'classes':('wide',),
      'fields':('email','password1','password2')}
     ),
    )

admin.site.register(Usuarios, UserAdmin)
