from django.test import TestCase
from django.urls import reverse


class GetCoockieViewTestCase(TestCase):
    def test_get_coockie_view(self):
        response = self.client.get(reverse("myauth:get_coockie"))
        self.assertContains(response,"Coockie set")
# Create your tests here.
