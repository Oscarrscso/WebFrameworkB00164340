from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    item_desc = models.TextField("description")
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.item_name