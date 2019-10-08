from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=128)
    email = models.EmailField(null=True)
    username_role = models.CharField(max_length=32)
    regTime = models.DateTimeField(null=True)
    userState = models.BooleanField(null=True)


class Role(models.Model):
    role_name = models.CharField(max_length=32)


class UserSoft(models.Model):
    soft = models.CharField(max_length=32, null=False)
    username = models.CharField(max_length=32)
