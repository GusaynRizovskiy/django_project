from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(null=False, blank=True)
