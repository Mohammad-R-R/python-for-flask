from django.db import models

class Book(models.Model):
    title= models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # list autor 


class Author(models.Model):
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes= models.TextField()
    books = models.ManyToManyField(Book, related_name="author")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def all_books():
   return Book.objects.all()

def add_book(t,desc):
   return Book.objects.create(title=t,description=desc)

def get_book(id):
    return Book.objects.get(id=id)

def get_authors(i):
    return get_book(i).author

def add_author_to_book(author_id,book_id):
    b=Author.objects.get(author_id=id)
    c=get_book(book_id)
    c.author.add(b)








