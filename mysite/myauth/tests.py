from django.test import TestCase
from django.urls import reverse


class GetCoockiesViewTestCase(TestCase):
    def test_get_coockies_view(self):
        response = self.client.get(reverse("myauth:get_cookie"))
        self.assertContains(response,"Set Coockie")
# Create your tests here.
class FooBarViewTest(TestCase):
    def test_foo_bar_view(self):
        response = self.client.get(reverse("myauth:foo-bar"))
        self.assertEqual(response.status_code,200)
        self.assertEqual(
            response.headers['content-type'],'application/json',
        )
        expected_data = {"foo":"bar","spam":"eggs"}
        self.assertJSONEqual(response.content,expected_data)