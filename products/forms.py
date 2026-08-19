from django import forms

from .models import Product


# ==========================================
# Form 2 - Django Form
# ==========================================

class ProductForm(forms.Form):

    name = forms.CharField(
        label="اسم المنتج",
        max_length=200
    )

    price = forms.DecimalField(
        label="السعر",
        max_digits=10,
        decimal_places=2
    )

    description = forms.CharField(
        label="الوصف",
        widget=forms.Textarea
    )


# ==========================================
# Form 3 - ModelForm
# ==========================================

class ProductModelForm(forms.ModelForm):

    class Meta:

        model = Product

        fields = [
            'category',
            'name',
            'description',
            'price',
            'quantity',
            'image',
            'available'
        ]

        labels = {
            'category': 'التصنيف',
            'name': 'اسم المنتج',
            'description': 'الوصف',
            'price': 'السعر',
            'quantity': 'الكمية',
            'image': 'الصورة',
            'available': 'متوفر'
        }

        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 4
                }
            )
        }