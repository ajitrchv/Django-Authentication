from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name}"
    
class Language(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
    

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey('Author',null=True, on_delete=models.SET_NULL)
    summary = models.TextField(max_length=600)
    isbn = models.CharField('ISBN', max_length=15, unique=True)
    genre = models.ManyToManyField(Genre)
    Language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    
    
    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    


    
class Author(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    dateofbirth = models.DateField(null=True, blank=True)
    class Meta:
        ordering=['lname', 'fname']
    
    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return f"{self.fname} {self.lname}"


import uuid

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book',null=True, on_delete=models.RESTRICT)  
    imprint = models.CharField(max_length=50)
    due_back = models.DateField(null=True,auto_now=False, auto_now_add=False)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank = True, default = 'm')
    class Meta:
        ordering = ['due_back']
    def __str__(self):
        return f"[{self.id}]: {self.book.title}"