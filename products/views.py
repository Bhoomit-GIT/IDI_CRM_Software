from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from django.views import View
from .forms import ProductModelForm


# Create your views here.

class ProductObjectMixin(object):
    model = Product

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj
    
class ProductUpdateView(ProductObjectMixin, View):
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
                form.save()
            context['object'] = obj
            context['form']   = form
        return render(request, self.template_name, context)

class ProductCreateView(View):
    template_name = "products/product_create.html"

    def get(self, request, id=None, *args, **kwargs):
        form = ProductModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)
    
    def post(self, request, id=None, *args, **kwargs):
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductModelForm()
        context = {'form': form}    
        return render(request, self.template_name, context)

class ProductListView(View):
    template_name = "products/product_list.html"
    queryset = Product.objects.all()

    def get_queryset(self):
        return self.queryset
    
    def get(self, request, *args, **kwargs):
        context = {'object_list' : self.get_queryset()}
        return render(request, self.template_name, context)

class MyListView(ProductListView):
    # queryset = Product.objects.filter(id=2)   
    queryset = Product.objects.all().order_by('-id') # - minus sign to reverse the order


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
            context['object'] = obj
            return redirect('/products/')
        return render(request, self.template_name, context)
    
class ProductDetailView(ProductObjectMixin, View):
    template_name = "products/product_detail.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)