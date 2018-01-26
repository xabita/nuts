# debes importar tu modelo de usuario, independiente de cual sea
from .models import UserCourse

class UserAuthentificacionBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = UserCourse.objects.get(username=username)
            # en este punto, debes verificar la contraseña, yo lo hare como lo hace el modelo de usuario de django, siguiendo los metodos que trae este
            if user.password == password:
            #if user.check_password(password):
                return user
        except UserCourse.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserCourse.objects.get(id=user_id)
        except:
            return None