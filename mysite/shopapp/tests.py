from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from string import ascii_letters
from random import choices

from shopapp.models import Product


# Create your tests here.
class ProductsCreateView(TestCase):
    def setUp(self):
        self.product_name = "".join(choices(ascii_letters,k=10))
        Product.objects.filter(name = self.product_name).delete
    def test_product_create(self):
        response = self.client.post(
            reverse("shopapp:product_create"),
            {
                "name": self.product_name,
                "description": "Good product",
                "price": 4300,
                "discount": 15
            }
        )
        self.assertRedirects(response, reverse("shopapp:products_list"))
        self.assertTrue(self.product_name)

class ProductsDetailsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product = Product.objects.create(name = "Bobina")
    @classmethod
    def tearDownClass(cls):
        cls.product.delete()
    def test_product_details(self):
        response = self.client.get(reverse("shopapp:products_details",kwargs={"pk":self.product.pk}))
        self.assertContains(response,self.product.name)

class ProductsListViewTestCase(TestCase):
    fixtures = [
        'shoapp-fixtures.json'
    ]
    def test_product_list(self):
        response = self.client.get(reverse("shopapp:products_list"))
        self.assertQuerySetEqual(
            qs=Product.objects.filter(archived = False).all(),
            values = [p.pk for p in response.context["product"]],
            transform = lambda p: p.pk
        )
class OrderViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.credentials = dict({"username":"Bob","password":"qwerty"})
        cls.user = User.objects.create_user(**cls.credentials)
    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
    def setUp(self):
        self.user.login(**self.credentials)
    def test_oredr_view(self):
        response = self.client.get(reverse('shopapp:orders_list'))
        self.assertContains(response,'Order')



