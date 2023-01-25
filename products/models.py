from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=250)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'