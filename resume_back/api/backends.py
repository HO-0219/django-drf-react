# accounts/backends.py

from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class CustomUserModelBackend(ModelBackend):
    def authenticate(self, request, user_id=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(user_id=user_id)
        except CustomUser.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None