from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from django.views import View
from .forms import ProductModelForm
from django.db import transaction

 
# Create your views here.

class ProductObjectMixin(object):
    model = Product

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj
    
class ProductCreateView(View):                          #By using previously deleted ids 
    template_name = "products/product_create.html"

    def get(self, request, id=None, *args, **kwargs):
        form = ProductModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)
    
    def post(self, request, id=None, *args, **kwargs):
        form = ProductModelForm(request.POST)
        if form.is_valid():
            all_ids = list(Product.objects.values_list('id', flat=True))
            new_id = 1  # Start at 1
            while new_id in all_ids:
                new_id += 1
            # form = ProductModelForm()         #Will redirect to again create form
            product = form.save(commit=False)
            product.id = new_id  # Set the new ID explicitly
            product.save()  # Now save the product
            return redirect('/products/')           #Redirect to list view after creating
        context = {'form': form}        
        return render(request, self.template_name, context)  
 

# class ProductCreateView(View):                          #By using default ids which are auto incrementing
#     template_name = "products/product_create.html"

#     def get(self, request, id=None, *args, **kwargs):
#         form = ProductModelForm()
#         context = {'form': form}
#         return render(request, self.template_name, context)
    
#     def post(self, request, id=None, *args, **kwargs):
#         form = ProductModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # form = ProductModelForm()
#             return redirect('/products/')
#         context = {'form': form}        
#         return render(request, self.template_name, context)    
    
class ProductUpdateView(ProductObjectMixin, View):    # Updating the product and saving it as a new product
    template_name = "products/product_update.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ProductModelForm(instance=obj)
            context['object'] = obj
            context['form']   = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):    
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ProductModelForm(request.POST, instance=obj)
            if form.is_valid():
                new_product = form.save(commit=False)
                new_product.id = None
                new_product.save()
                return redirect('/products/')
            context['object'] = obj
            context['form']   = form
        return render(request, self.template_name, context)    
    
# class ProductUpdateView(ProductObjectMixin, View):     # Updating the product
#     template_name = "products/product_update.html"

#     def get(self, request, id=None, *args, **kwargs):
#         context = {}
#         obj = self.get_object()
#         if obj is not None:
#             form = ProductModelForm(instance=obj)
#             context['object'] = obj
#             context['form']   = form
#         return render(request, self.template_name, context)

#     def post(self, request, id=None, *args, **kwargs):    
#         context = {}
#         obj = self.get_object()
#         if obj is not None:
#             form = ProductModelForm(request.POST, instance=obj)
#             if form.is_valid():
#                 form.save()
#             context['object'] = obj
#             context['form']   = form
#         return render(request, self.template_name, context)

class ProductDeleteView(ProductObjectMixin, View):
    template_name = "products/product_delete.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            def delete(self, *args, **kwargs):
                self.is_deleted = True
                self.save()
            context['object'] = obj
            return redirect('/products')
        return render(request, self.template_name, context)   

class ProductListView(View):
    template_name = "products/product_list.html"
    queryset = Product.objects.all()

    def get_queryset(self):
        return self.queryset.filter(is_deleted = False)
    
    def get(self, request, *args, **kwargs):
        context = {'object_list' : self.get_queryset()}
        return render(request, self.template_name, context)

class MyListView(ProductListView):
    # queryset = Product.objects.filter(id=2)   
    queryset = Product.objects.all().order_by('id') # - minus sign to reverse the order

class ProductDetailView(ProductObjectMixin, View):
    template_name = "products/product_detail.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)