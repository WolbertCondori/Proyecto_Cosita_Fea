import secrets

from django.db import models

class EstadoChoises(models.TextChoices):
    PROCESS = "PRO", "Proceso"
    COMPLET = "COM", "Completado"
    EXPIRE = "EXP", "Expirado"
    CANCEL = "CAN", "Cancelado"


class Pacientes(models.Model):
    nombre = models.TextField(max_length=30,null=False,blank=False,verbose_name="Nombre")
    nie = models.PositiveIntegerField()
    estado = models.TextField(choices=EstadoChoises.choices,default=EstadoChoises.PROCESS,verbose_name="Estado")
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Entonces creamos slug unico
            prov = secrets.token_hex(16)
            while Pacientes.objects.filter(slug=prov).exists():
                prov = secrets.token_hex(16)
            self.slug = prov
        super().save(*args, **kwargs)


    class Meta:
        db_table = 'Pacientes'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ('slug',)

    def __str__(self):
        return self.slug