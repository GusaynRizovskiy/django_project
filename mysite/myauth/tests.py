import json

from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class GetCoockieViewTestCase(TestCase):
    def test_get_coockie(self):
        response = self.client.get(reverse("myauth:get_coockie"))
        self.assertContains(response,'Coockie get')

class FooBarViewTestCase(TestCase):
    def test_foo_bar(self):
        response = self.client.get(reverse("myauth:foo-bar"))
        just_date = json.loads(response.content)
        recieved_date = {"fruit":"apple","orange":"bananas"}
        self.assertEqual(response.status_code,200)
        self.assertEqual(just_date,recieved_date)


