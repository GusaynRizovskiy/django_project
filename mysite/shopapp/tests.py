from django.test import TestCase
from django.urls import reverse
from string import ascii_letters
from random import choices

from shopapp.models import Product


# Create your tests here.

class ProductCreateViewTestCase(TestCase):
    def setUp(self):
        self.product_name = "".join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete
    def test_product_create(self):

        response = self.client.post(
            reverse('shopapp:product_create'),
            {
                "name": self.product_name,
                "description":"Good food",
                "price":2340,
                "discount":10
            }
        )
        self.assertRedirects(response, reverse("shopapp:products_list"))

class ProductDetailsViewTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Best product")
    def tearDown(self):
        self.product.delete()
    def test_product_details(self):
        response = self.client.get(
            reverse('shopapp:products_details',kwargs={"pk":self.product.pk})
        )
        self.assertEqual(response.status_code,200)