from django.db import models


class UserAccount(models.Model):

    full_name = models.CharField(max_length=150)

    username = models.CharField(
        max_length=100,
        unique=True
    )

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20)

    password = models.CharField(max_length=128)

    address = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name