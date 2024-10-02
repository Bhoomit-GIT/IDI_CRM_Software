from django.shortcuts import render,get_object_or_404,redirect
from .models import Connection
from django.views import View
from .forms import ConnectionModelForm

# Create your views here.

class ConnectionObjectMixin(object):
    model = Connection

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj

class ConnectionCreateView(View):
    template_name = "connections/connection_create.html"

    def get(self, request, id=None, *args, **kwargs):
        form = ConnectionModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):
        form = ConnectionModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = ConnectionModelForm()
        context = {'form': form}    
        return render(request, self.template_name, context)     

class ConnectionUpdateView(ConnectionObjectMixin, View):
    template_name = "connections/connection_update.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ConnectionModelForm(instance=obj)
            context['object'] = obj
            context['form']   = form
        return render(request, self.template_name, context)

    def post(self, request, id=None, *args, **kwargs):    
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ConnectionModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form']   = form
        return render(request, self.template_name, context)   

class ConnectionDeleteView(ConnectionObjectMixin, View):
    template_name = "connections/connection_delete.html"

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
            return redirect('/connection/')
        return render(request, self.template_name, context)    
    
class ConnectionListView(View):
    template_name = "connections/connection_list.html"
    queryset = Connection.objects.all()

    def get_queryset(self):
        return self.queryset
    
    def get(self, request, *args, **kwargs):
        context = {'object_list' : self.get_queryset()}
        return render(request, self.template_name, context)

class MyListView(ConnectionListView):
    # queryset = Product.objects.filter(id=2)   
    queryset = Connection.objects.all().order_by('-id') # - minus sign to reverse the order

class ConnectionDetailView(ConnectionObjectMixin, View):
    template_name = "connections/connection_detail.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)