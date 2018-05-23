from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=600)
    
    def __str__(self):
        return (self.name)
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=1)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return (self.name)

class Order(models.Model):
    date_order = models.DateTimeField('date order')
    date_ship = models.DateTimeField('date ship')
    number = models.IntegerField(default=1)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    
