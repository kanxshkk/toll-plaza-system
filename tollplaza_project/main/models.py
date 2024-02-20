# main/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    car_number = models.CharField(max_length=20, unique=True)
    money_in_ewallet = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    # Add the related_name attribute to avoid conflicts
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_permissions',
    )

    def __str__(self):
        return self.username


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_number = models.CharField(max_length=20)
    toll_fee = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.car_number} - {self.toll_fee} - {self.timestamp}"
