from django.shortcuts import render,HttpResponseRedirect
from practice.forms  import *
from .models import Product
from django.views.generic.list import ListView

def formp(request):
    print("form")
    if request.method == "GET":
        form = ProductForm(request.GET)
        
        print(form)
        
        if(form.is_valid()):
#             print("hop le")
            form.save()

            return HttpResponseRedirect('/practice/list')
    return render(request, 'product/form.html', {'form': form})
 
class ListProduct(ListView):
    product = Product
    paginate_by = 10
    context_object_name = "products"
    queryset = Product.objects.all()
    
    template_name = 'product/list.html'
    
            
        
