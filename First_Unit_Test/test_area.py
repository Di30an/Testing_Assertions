from unittest import TestCase
import area


class TestShapeAreas(TestCase):

    def test_triangle_area(self):
        self.assertEqual(10, area.triangle_area(4,5))