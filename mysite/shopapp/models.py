from django.contrib.auth.models import User
from django.db import models

def product_preview_directory_path(instance: "Product",filename = str)->str:
    return "products/product_{pk}/previw/{filename}".format(
        pk = instance.pk,
        filename = filename
    )
class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0,max_digits=8,decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=0)
    preview = models.ImageField(null=True,blank=True,upload_to=product_preview_directory_path)
    def __str__(self) -> str:
        return f"Product(pk = {self.pk}, name = {self.name!r})"

class Order(models.Model):
    delivery_address = models.TextField(null=True, blank=True)
    promocode = models.CharField(max_length=24,null=False,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='orders')
    receipt = models.FileField(null=True, upload_to='orders/receipts')
