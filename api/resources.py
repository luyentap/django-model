from tastypie.resources import ModelResource
from practice.models import Product,Category
import tastypie
from django.contrib.admin import models

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        allowed_methods = ['get']

class MyModelResource(ModelResource):
    category = tastypie.fields.ForeignKey(CategoryResource, 'category', full=True)
    class Meta:
        queryset = Product.objects.all()
        allowed_methods = ['get'] #method of http
        resource_name = 'product' #http://localhost:8000/api/v1/product
#         excludes = ["price"] #không bao gồm

