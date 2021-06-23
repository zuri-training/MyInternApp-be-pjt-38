from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class ViewBaseTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ViewBaseTests, cls).setUpClass()
        # cls.client = Client()
        # cls.another_client = Client()
        cls.unlogged_client = Client()


class LoggedOutUserTests(ViewBaseTests):
    def setUp(self):
        super(LoggedOutUserTests, self).setUp()

    def test_home(self):
        resp = self.unlogged_client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "backend/index.html")

