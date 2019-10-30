from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20,default=None)

class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    mob = models.IntegerField()
    fk_login = models.ForeignKey(Login, on_delete=models.CASCADE, default=None)   