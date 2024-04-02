from django.test import TestCase
from django.urls import reverse
from string import ascii_letters
from random import choices
from .models  import Product

# Create your tests here.
class ProductCreateViewTestCase(TestCase):
    def setUp(self):
        self.product_name = "".join(choices(ascii_letters,10))
        Product.objects.filter(name = self.product_name).delete()
    def test_create_product(self):
        response = self.client.post(
            reverse("shopapp:product_create"),

            {
                "name":self.product_name,
                "description":"a good thing",
                "price":123,
                "discount":345
            }
        )
        self.assertRedirects(response,reverse("shopapp:products_list"))
        self.assertTrue(
            Product.objects.filter(name=self.product_name).exists()
        )
class ProductDetailsViewTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.product = "".join(choices(ascii_letters,10))
    @classmethod
    def tearDown(cls):
        cls.product.delete()
    def test_get_product_and_check_content(self):
        response = self.client.get(
            reverse("shopapp:product_details",kwargs={"pk":self.product.pk})
        )
        self.contains(response,self.product.name)