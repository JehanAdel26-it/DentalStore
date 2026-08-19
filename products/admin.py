from django.contrib import admin
from .models import Category, Product, ProductType


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'price',
        'quantity',
        'available'
    )

    list_filter = (
        'category',
        'available'
    )

    search_fields = (
        'name',
        'description'
    )


# ==========================================
# Product Type
# ==========================================

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'description',
        'created_at'
    )

    search_fields = (
        'name',
        'description'
    )