from django.contrib import admin

from Historial.models import Citas


class CitasAdmin(admin.ModelAdmin):
    list_display = ("nie","fecha","estado","creado","actualizado","slug",)
    list_filter = ("nie","fecha","estado",)
    search_fields = ("nie","estado",)
    readonly_fields = ('slug',)

    list_per_page = 25

    fieldsets = (
    ("Informacion",{'fields':("nie","fecha","slug",)}),
    ("Configuracion",{'fields':("estado",)})
    )
admin.site.register(Citas,CitasAdmin)