from django.db import models
import re	# the regex module


class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["name2"] = "first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["name"] = "last name should be at least 5 characters"
        if len(postData['password']) < 8:
            errors["desc"] = "password  should be at least 10 characters"

        if postData["password"]!=postData['confirm'] :
            errors['2000cc']='the password dosnt match'
        if Users.objects.filter(email=postData['email']):
            errors['in']='email in use'

        return errors

    def basic_validator2(self, postData):
        errors2 = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['email2']) < 10:
            errors2["desc"] = "password  should be at least 10 characters"

        if len(postData["password1"])<10 :
            errors2['2000cctarbu']='u have to write 10 char at least '
        return errors2
    
    


        
class BookManager(models.Manager):
    def basic_validator(self, postData):    
        errors = {}
        print("IN the models: %s" % postData)
        if len(postData['title'])<1:
            errors['one']='u have to enter at least 1 char'
        if len(postData['desc'])<10:
            errors['two']='u have to enter at least 10 char'
        return errors


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=BlogManager()


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc=models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by=models.ForeignKey(Users,related_name="books_uploaded",on_delete=models.CASCADE)
    users_who_like=models.ManyToManyField(Users,related_name="liked_books")
    objects=BookManager()





