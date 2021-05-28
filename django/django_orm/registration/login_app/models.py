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
        return errors

    def basic_validator2(self, postData):
        errors2 = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['email2']) < 10:
            errors2["desc"] = "password  should be at least 10 characters"

        if len(postData["password1"])<10 :
            errors2['2000cctarbu']='the password dosnt match'
        return errors2
    
    


        
    class BlogManager(models.Manager):
        def basic_validator(self, postData):    
            errors = {}
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
                errors['email'] = "Invalid email address!"
            return errors


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=BlogManager()




# def register(username,password):
#     Users.objects.create(name=username,password=password)

# def check_user(name,passed):
#     user=Users.objects.filter(name=name)
#     if user == None:
#         return False
#     if user[0].password == passed:
#         return True
#     return False