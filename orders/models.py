
from django.db import models
from django.contrib.auth.models import User


class DesignService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class DesignOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='design_orders'
    )
    service = models.ForeignKey(
        DesignService,
        on_delete=models.PROTECT,
        related_name='orders'
    )
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
