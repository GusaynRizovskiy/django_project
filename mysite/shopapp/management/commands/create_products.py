from django.core.management import BaseCommand
from shopapp.models import Product
class Command(BaseCommand):
    """
    Create products
    """
    def handle(self, *args, **options):
        products_name = [
            "Laptop",
            "Smartphone",
            "Television"
        ]
        for product_name in products_name:
            product,created = Product.objects.get_or_create(name= product_name)
            self.stdout.write(f"Create product {product.name}")
        self.stdout.write(self.style.SUCCESS("Created product"))