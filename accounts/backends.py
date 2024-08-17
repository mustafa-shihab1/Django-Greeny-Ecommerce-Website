from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpRequest

# create middleware to login with username or (email)

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            ## start search with username then email
            user = User.objects.get(
                Q(username__iexact=username) |
                Q(email__iexact=username)
            )
        except User.DoesNotExist:
            pass
        ## if return more than one user get the first
        except User.MultipleObjectsReturned:            
            return User.objects.filter(email=username).order_by('id').first()
        else:
            ## if user exist then check password and authentication here and return user
            if user.check_password(password) & self.user_can_authenticate(user):
                return user
            

    # def get_user(self, user_id):
    #     try:
    #         user = User.objects.get(pk=user_id)
    #     except User.DoesNotExist:
    #         raise None
        
    #     return super().get_user(user_id)