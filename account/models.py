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


# ==========================================
# Profile - علاقة One To One
# ==========================================

class Profile(models.Model):

    user = models.OneToOneField(
        UserAccount,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    bio = models.TextField(
        blank=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return f"Profile - {self.user.full_name}"