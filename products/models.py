from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=200)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.PositiveIntegerField()

    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # ===========================
    # Product Type Model
    # ===========================


class ProductType(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ===========================
# Many To Many Relationship
# ===========================

Product.add_to_class(
    'product_types',
    models.ManyToManyField(
        ProductType,
        blank=True
    )
)


# ===========================
# One To One Relationship
# ===========================

class ProductDetails(models.Model):

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='details'
    )

    manufacturer = models.CharField(
        max_length=150,
        blank=True
    )

    warranty = models.CharField(
        max_length=100,
        blank=True
    )

    specifications = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"تفاصيل {self.product.name}"