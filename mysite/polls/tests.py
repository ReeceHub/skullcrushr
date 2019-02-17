from django.test import TestCase
from django.urls import resolve
from polls.views import index

class Index(TestCase):

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/polls/')
        self.assertEqual(found.func, index)
