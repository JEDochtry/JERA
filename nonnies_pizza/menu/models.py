from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.name

