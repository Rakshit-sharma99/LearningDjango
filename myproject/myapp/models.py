from django.db import models

# Create your models here.
class Emp(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    salary = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Author(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    description=models.CharField(max_length=250)
    def __str__(self):
        return self.name
class Book(models.Model):
    title=models.CharField(max_length=250)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    published_date=models.DateField()
    def __str__(self):
        return self.title