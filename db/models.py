from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True,verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Цена")
    choose = models.BooleanField(default=False,verbose_name="Добавить в корзину")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"