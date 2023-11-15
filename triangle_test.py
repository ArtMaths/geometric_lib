from triangle import area
from triangle import perimeter
import unittest

class TriangleTestCase(unittest.TestCase):
   def test_triangle_area1(self):
       res = area(5, 3)
       self.assertEqual(res, 7.5)
       
   def test_triangle_area2(self):
       res = area(0.1256, 0.64748)
       self.assertEqual(res, 0.040661744)

   def test_triangle_perimeter1(self):
       res = perimeter(3, 4, 6)
       self.assertEqual(res, 13)

   def test_triangle_perimeter2(self):
       res = perimeter(0.1384329, 0.5537316, 0.040661744)
       self.assertEqual(res, 0.732826244)