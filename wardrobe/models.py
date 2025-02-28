from django.db import models

# Create your models here.
class ClothingItem(models.Model):
    OCCASION_CHOICES = [
        ('casual', 'Casual'),
        ('formal', 'Formal'),
        ('sports', 'Sports'),
        ('party', 'Party'),
    ]

    brand = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    purchase_date = models.DateField()
    size = models.DecimalField(decimal_places=2, max_digits=10)
    occasion = models.CharField(max_length=100)

    def __str__(self):
        return self.brand - self.occasion
