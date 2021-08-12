from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__ (self):
        return(self.name)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    catagory = models.ForeignKey(Catagory, on_delete =CASCADE)
    def __str__ (self):
        return(self.name)

class Review(models.Model):
    name =models.CharField(max_length=200)
    email = models.EmailField()
    review = models.TextField()
    product =models.ForeignKey(Product, on_delete=CASCADE)
    def __str__ (self):
        return(self.name)