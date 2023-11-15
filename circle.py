import math
import unittest

def area(r):
    '''Функция получает на вход число r (радиус круга), а на выходе возвращает площадь данного круга'''
    return math.pi * r * r


def perimeter(r):
    '''Функция получает на вход число r (радиус круга), а на выходе возвращает периметр данного круга'''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
   def test_circle_area1(self):
       res = area(5)
       self.assertEqual(res, 78.53981633974483)
       
   def test_circle_area2(self):
       res = area(0.64748)
       self.assertEqual(res, 1.3170509889785151)

   def test_circle_perimeter1(self):
       res = perimeter(6)
       self.assertEqual(res, 37.69911184307752)

   def test_circle_perimeter2(self):
       res = perimeter(0.1384329)
       self.assertEqual(res, 0.869799563310261)



