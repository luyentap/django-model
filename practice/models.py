from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from _datetime import datetime
from random import choice


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=600)
    
    def __str__(self):
        return (self.name)
    def get_category_name(self):
        return "abc";
        
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_category_name')

 
class Order(models.Model):
    STATUS_CHOICES = (
    (1,'one'),
    (2,'two'),
)   
  
    date_order = models.DateTimeField('date order')
    date_ship = models.DateTimeField('date ship')
    number = models.IntegerField(default=1,choices=STATUS_CHOICES)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    


#     ●    Create a custom QuerySet that only get products with Category = “Car”
class ProductQuerySet(models.QuerySet):
    def get_product_car(self):
        """
        get category_id có tên = "car" 
        sau đó filter trong product có mã category tương ứng
        """
        category_id_filter = Category.objects.filter(name="car")[0].id;
        return self.filter(category_id=category_id_filter)
    
# ●    Create a custom Manager that only get products have quantity > 5
class ProductManager(models.Manager):
    def get_product(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT id,name,price,category_id,number FROM `practice_product` 
            WHERE number>5""")
             
            list_product = []
            for row in cursor.fetchall():
                product = self.model(id=row[0],name=row[1],price=row[2],category_id=row[3])
                product.number = row[4]
                list_product.append(product)
                 
        return list_product
    
    #get queryset
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    #using queryset
    def get_product_from_queryset(self):
        return self.get_queryset().get_product_car()


class PRawSql():
    def get(self):
# ●    Try to use Raw SQL to get products with Category = “Car”
        product_list = Product.objects.raw(""" 
        SELECT practice_product.id,practice_product.name FROM `practice_product` INNER join practice_category on practice_category.id = practice_product.category_id 
            WHERE  practice_category.name='car'""")
         
        return product_list
    
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=1)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    #thêm custom manager--> dùng api qua model
    manage = ProductManager()

    # do đã custom manager  -->phải thêm vào mới test model Product qua api như bình thường được
    #đối tượng đó nên  tên là objects~~
    objects = models.Manager()
    
    #nếu muốn gọi thẻn không cần qua custom manager
    queryset = ProductQuerySet.as_manager()
    
    #rawSql
    raw = PRawSql()
    
    def __str__(self):
        return (self.name)
    
    def get_object_all(self):
        return Product.objects.all()
