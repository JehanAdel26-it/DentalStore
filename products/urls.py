from django.urls import path

from . import views


urlpatterns = [

    # ==========================================
    # الصفحة الرئيسية
    # ==========================================

    path(
        '',
        views.home,
        name='home'
    ),


    # ==========================================
    # Forms
    # ==========================================

    # Form 1 - HTML
    path(
        'product-form-html/',
        views.product_form_html,
        name='product_form_html'
    ),

    # Form 2 - Django Form
    path(
        'product-form/',
        views.product_form_django,
        name='product_form_django'
    ),

    # Form 3 - ModelForm
    path(
        'product-modelform/',
        views.product_form_modelform,
        name='product_form_modelform'
    ),


    # ==========================================
    # Relationships
    # ==========================================

    # One To One
    path(
        'one-to-one/',
        views.one_to_one_view,
        name='one_to_one'
    ),

    # Many To Many
    path(
        'many-to-many/',
        views.many_to_many_view,
        name='many_to_many'
    ),


    # ==========================================
    # QuerySet
    # ==========================================

    path(
        'querysets/',
        views.querysets_view,
        name='querysets'
    ),


    # ==========================================
    # CRUD
    # ==========================================

    # Read
    path(
        'products/',
        views.product_list,
        name='product_list'
    ),

    # Create
    path(
        'products/create/',
        views.product_create,
        name='product_create'
    ),

    # Update
    path(
        'products/<int:product_id>/edit/',
        views.product_update,
        name='product_update'
    ),

    # Delete
    path(
        'products/<int:product_id>/delete/',
        views.product_delete,
        name='product_delete'
    ),

]