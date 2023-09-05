from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, password, **kwargs):
        user = self.model(password=password, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create(self, **kwargs):
        return self.create_user(**kwargs)


    def create_superuser(self,password,  **kwargs):
        user = self.model(**kwargs)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
    


class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username