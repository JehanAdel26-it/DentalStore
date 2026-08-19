from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('products.urls')),

    path('account/', include('account.urls')),

    path('categories/', include('categories.urls')),

    path('product-types/', include('product_types.urls')),
]