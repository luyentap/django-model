from tastypie.resources import ModelResource
from practice.models import Product,Category
import tastypie
from django.contrib.admin import models
from .cache1 import JSONCache
from tastypie.cache import SimpleCache

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        allowed_methods = ['get']
        #Implementing Your Own Cache from cache1.py
        cache = JSONCache()

class MyModelResource(ModelResource):
    category = tastypie.fields.ForeignKey(CategoryResource, 'category', full=True)
    class Meta:
        queryset = Product.objects.all()
        allowed_methods = ['get'] #method of http
        resource_name = 'product' #http://localhost:8000/api/v1/product
#         excludes = ["price"] #không bao gồm
        # cache option.
        cache = SimpleCache(timeout=10)

