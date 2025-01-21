from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Dish(models.Model):
    CATEGORY_CHOICES = [
        ('drink', 'Напиток'),
        ('main', 'Основное блюдо'),
        ('dessert', 'Десерт'),
        ('appetizer', 'Закуска'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='main'
    )

    def __str__(self):
        return self.name