from django.db import models

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 5:
            errors["title"] = "Blog name should be at least 5 characters"
        if len(postData['Description']) < 10:
            errors["Description"] = "Blog description should be at least 10 characters"

        if len(postData['Network']) < 10:
            errors["network"] = "Blog network should be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    date = models.DateTimeField()
    Description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BlogManager()







# def addshow(t,net,date,desc):
#     show.objects.create(title=t,network=net,date=date,Description=desc)

# def show_table(id):
#     show.objects.create(id=id)    
        













