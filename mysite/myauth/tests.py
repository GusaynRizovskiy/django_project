from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class GetCoockieViewTestCase(TestCase):
    def test_get_coockie(self):
        response = self.client.get(reverse("myauth:get_coockie"))
        self.assertContains(response,"Coockie get")

class FooBarViewTestCase(TestCase):
    def test_foo_bar(self):
        response = self.client.get(reverse("myauth:foo-bar"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response.headers['content-type'],'application/json')
        expected_date = {"putin":"good","baiden":"evil"}
        self.assertEqual(response.content,expected_date)