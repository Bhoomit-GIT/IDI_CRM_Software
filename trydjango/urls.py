"""
URL configuration for Invoice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.views.generic import TemplateView
# from appInvoice.views import home,about,initial_product_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="base.html"), name="home"),
    # path('about/', about,name='Invoice-about'),
    # # path('create/', create_product_view,name='create_product_view'),
    # path('create/<int:product_id>/', initial_product_view,name='initial_product_view'),
    path('products/',include('products.urls')),
    path('connection/',include('connections.urls')),
    path('invoice/',include('invoice.urls'))
]
