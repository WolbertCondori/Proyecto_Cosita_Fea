from .users_model import Usuarios, RolChoises
from .citas_model import Citas,EstadoChoises

for user in Usuarios.objects.filter(rol=RolChoises.DOCTOR):
    user.is_staff = True
    user.is_superuser = True
    user.save()