from django.db import models
from datetime import datetime

class Goods(models.Model):
    name = models.CharField("Назва товару", max_length=50)
    price = models.PositiveSmallIntegerField("Ціна товару", default=0, help_text="Сума у гривнях")
    color = models.CharField("Колір", max_length=20)
    description = models.TextField("Опис товару", max_length=500)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Додати товар у магазин"
        verbose_name_plural = "Додати товар у магазин"