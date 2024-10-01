from django.shortcuts import render,get_object_or_404,redirect
from .forms import rawproduct,ProductForm
from .models import Product

# Create your views here.

Invoices = [
    {
        'product_name' : 'Carbonation Chamber',
        'product_price' : '50000',
        'product_description' : 'Used for carbon fusioning'
    },
    {
        'product_name' : 'Industrial Ovens',
        'product_price' : '80000',
        'product_description' : 'Used for heating'
    }
]

def home(request):
    context = {
        'Invoices' : Invoices
    }
    return render(request,'login.html',context)

def about(request): 
    return render(request,'about.html',{'title':'about'})


def initial_product_view(request,product_id):
    product     =   get_object_or_404(Product,id = product_id)
    if request.method == 'POST':
        # Process the form submission (e.g., saving the updated data)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page after saving
    else:
        # Render the form with data from the product instance
        form = ProductForm(instance=product)

    return render(request, 'create.html', {'form': form})



# def initial_product_view(request):
#     obj = Product.objects.get(id=6)
#     my_form = productform(request.POST or None,instance=obj)
#     if my_form.is_valid():
#         my_form.save()
#     context = {
#         "form" : my_form
#     }
#     return render(request,'create.html',context)

# def create_product_view(request):

#     my_form = rawproduct(request.POST)
#     if my_form.is_valid():
#         print(my_form.cleaned_data)
#         Product.objects.create(**my_form.cleaned_data)
#     context = {
#         "form" : my_form
#     }
#     return render(request,'create.html',context)