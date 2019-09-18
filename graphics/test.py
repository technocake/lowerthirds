from django.test import TestCase


class DummyTestCase(TestCase):
    def test_nothing(self):
        self.assertEqual(1, 1)

