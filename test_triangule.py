import unittest

from triangle import triangle


class TestTriangule(unittest.TestCase):
    def test_equilateral(self):
        msg = 'Equilateral triangle'

        self.assertEquals(triangle(2, 2, 2), msg)

    def test_scalene(self):
        msg = 'Scalene triangle'

        self.assertEquals(triangle(2, 3, 4), msg)

    def test_isosceles_triangle(self):
        msg = 'Isosceles triangle'

        self.assertEquals(triangle(2, 2, 3), msg)
        self.assertEquals(triangle(3, 2, 2), msg)
        self.assertEquals(triangle(2, 3, 2), msg)
