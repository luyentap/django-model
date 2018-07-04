from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)

# all site:  disable delete selected, ngoại trừ product: set actions = [make_published,'delete_selected']
admin.site.disable_action('delete_selected')

def make_published(modeladmin, request, queryset):
    queryset.update(number=0)
    
make_published.short_description = "set number product=0"

@admin.register(Product)
class Product(admin.ModelAdmin):
    fields = ('name','price','number','category')
    empty_value_display = '-empty-'
    def save_model(self, request, obj, form, change):
        print("--saving--")
        print(form)
        obj.user = request.user
        super().save_model(request, obj, form, change)
        
    #change template
    change_form_template = "admin/product/change_form.html"
    
    #admin action:update
    actions = [make_published,'delete_selected']