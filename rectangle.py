import unittest

def area(a, b):
	'''Функция получает на вход числa a и b (стороны прямоугольника), а на выходе возвращает площадь данного прямоугольника'''
	return a * b

def perimeter(a, b):
	'''Функция получает на вход числa a и b (стороны прямоугольника), а на выходе возвращает периметр данного прямоугольника'''
	return 2 * (a + b)

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



