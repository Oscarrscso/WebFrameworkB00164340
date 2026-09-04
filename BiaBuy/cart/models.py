from django.db import models

# Create your models here.
class Cart(models.Model):
    cart = models.CharField(max_length=200)
    def __str__(self):
        return self.cart