from django.db import models


class EstadoChoises(models.TextChoices):
    PROCESS = "PRO", "Proceso"
    COMPLET = "COM", "Completado"
    EXPIRE = "EXP", "Expirado"
    CANCEL = "CAN", "Cancelado"

class Citas(models.Model):
    nie = models.ForeignKey("Usuarios", on_delete=models.DO_NOTHING,null=False, blank=False, related_name="NIE")
    estado = models.TextField(choices=EstadoChoises.choices, default=EstadoChoises.PROCESS, verbose_name="Estado")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")
