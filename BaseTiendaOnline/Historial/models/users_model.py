import secrets
from email.policy import default
from random import choices
from tabnanny import verbose

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

class RolChoises(models.TextChoices):
    DOCTOR = "DOC", "Doctor"
    PACIENTE = "PAC", "Paciente"

class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email or "@" not in email:
            raise ValueError('Usuario debe tener un correo valido')
        if not password:
            raise ValueError('Contraseña no valida')
        if any(ext in email for ext in settings.EXTENSIONES_BLACKLIST):
            raise ValueError(f'No te voy a dejar crear una cuenta. Formatos no permitidos: '+', '.join(settings.EXTENSIONES_BLACKLIST))
        email=self.normalize_email(email)
        extra_fields['email']=email
        rol = extra_fields.get("rol", RolChoises.PACIENTE)

        # Si es doctor, automáticamente es staff y superuser
        if rol == RolChoises.DOCTOR:
            extra_fields["is_staff"] = True
            extra_fields["is_superuser"] = True
        else:
            extra_fields["is_staff"] = False
            extra_fields["is_superuser"] = False

        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('rol', RolChoises.DOCTOR)

        if extra_fields.get('is_staff'):
            raise ValueError('Superuser debe tener is_staff=True.')

        if extra_fields.get('is_superuser'):
            raise ValueError('Superuser debe tener is_superuser=True.')

        if not password:
            raise ValueError('Contraseña no valida')

        return self.create_user(email, password, **extra_fields)



class Usuarios(AbstractBaseUser,PermissionsMixin):
    nombre = models.CharField(unique=False,max_length=30,null=False,blank=False,verbose_name="Nombre")
    email = models.EmailField(unique=True, max_length=254,null=False,blank=False,verbose_name="Email")
    telefono = models.CharField(max_length=11,null=True,blank=True,verbose_name="Telefono")
    nie = models.CharField(max_length=10,unique=True,null=False,blank=False,verbose_name="NIE")
    nc = models.CharField(max_length=10,unique=True,null=True,blank=True,verbose_name="NC")
    fecha_nacimiento = models.CharField(null=False,blank=False,verbose_name="Fecha de nacimiento")
    edad = models.PositiveIntegerField(null=False,blank=False,verbose_name="Edad")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")
    rol = models.CharField(choices=RolChoises.choices,default=RolChoises.PACIENTE,verbose_name="ROL")

    #para el admin
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        # Si el rol es doctor, es superuser y staff
        if self.rol == RolChoises.DOCTOR:
            self.is_staff = True
            self.is_superuser = True
        else:
            # Si no es doctor, no es superuser ni staff
            self.is_staff = False
            self.is_superuser = False

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'Usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ('nie',)

    def __str__(self):
        return self.nie