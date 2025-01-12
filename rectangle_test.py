from rectangle import area
from rectangle import perimeter
import unittest

class RectangleTestCase(unittest.TestCase):
   def test_rectangle_area1(self):
       res = area(5, 3)
       self.assertEqual(res, 15)
       
   def test_rectangle_area2(self):
       res = area(0.1256, 0.64748)
       self.assertEqual(res, 0.081323488)

   def test_rectangle_perimeter1(self):
       res = perimeter(3, 6)
       self.assertEqual(res, 18)

   def test_rectangle_perimeter2(self):
       res = perimeter(0.1384329, 0.5537316)
       self.assertEqual(res, 1.384329)