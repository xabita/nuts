# debes importar tu modelo de usuario, independiente de cual sea
from .models import UserCourse

class UserAuthentificacionBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = UserCourse.objects.get(username=username)
            if user.check_password(password):
                return user
        except UserCourse.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserCourse.objects.get(id=user_id)
        except:
            return None