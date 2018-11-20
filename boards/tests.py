from django.test import TestCase


class FirstTests(TestCase):
    def test_1_e_1(self):
        self.assertEquals(1, 1)

class SecondTests(TestCase):
    def test_2_e_2(self):
        self.assertEquals(1, 1)