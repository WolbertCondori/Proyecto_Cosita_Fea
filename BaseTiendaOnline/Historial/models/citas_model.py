import secrets

from django.db import models


class EstadoChoises(models.TextChoices):
    PROCESS = "PRO", "Proceso"
    COMPLET = "COM", "Completado"
    EXPIRE = "EXP", "Expirado"
    CANCEL = "CAN", "Cancelado"

class Citas(models.Model):
    nie = models.ForeignKey("Usuarios", on_delete=models.CASCADE,null=False, blank=False, related_name="NIE")
    fecha = models.DateTimeField(default="",blank=False,null=False)
    estado = models.TextField(choices=EstadoChoises.choices, default=EstadoChoises.PROCESS, verbose_name="Estado")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    def save(self, *args, **kwargs):
        if not self.slug:
            # Entonces creamos slug unico
            prov = secrets.token_hex(16)
            while Citas.objects.filter(slug=prov).exists():
                prov = secrets.token_hex(16)
            self.slug = prov

        super().save(*args, **kwargs)

    class Meta:
        db_table = "citas"
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        ordering = ['-creado']

    def __str__(self):
        return self.slug