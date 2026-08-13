from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='product_types_home'),
]