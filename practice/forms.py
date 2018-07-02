from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    price = forms.IntegerField
    number = forms.IntegerField
    category_id = forms.CharField
    
    class Meta:
        model = Product
        fields = ['name', 'price', 'category','number']
    
