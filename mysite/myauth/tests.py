import json

from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class GetCoockieViewTestCase(TestCase):
    def test_get_coockie(self):
        response = self.client.get(reverse("myauth:get_coockie"))
        self.assertContains(response,"Coockie get")

class FooBarViewTestCase(TestCase):
    def test_foo_bar(self):
        responose = self.client.get(reverse("myauth:foo-bar"))
        self.assertEqual(responose.status_code,200)
        expected_date = {"foobar": "bananos","looka":"potatos"}
        revieved_date = json.loads(responose.content)
        self.assertEqual(revieved_date,expected_date)
