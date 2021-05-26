from django.db import models

class user(models.Model):
    name=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def register(name, passwordd):
    user.objects.create(username= name, password= passwordd)

def check_user (name,passwordd):
    user_name=user.objects.filter(username=name)
    if user_name==None:
        return False
    if user_name.password == passwordd:
        return True

    return False