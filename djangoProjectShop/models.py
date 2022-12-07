from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    choose = models.BooleanField(default=False)

    def __str__(self):
        return self.name