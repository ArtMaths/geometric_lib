import unittest

def area(a):
    '''Функция получает на вход число a (сторона квадрата), а на выходе возвращает площадь данного квадрата'''
    return a * a


def perimeter(a):
    '''Функция получает на вход число a (сторона квадрата), а на выходе возвращает периметр данного квадрата'''
    return 4 * a

class SquareTestCase(unittest.TestCase):
   def test_square_area1(self):
       res = area(5)
       self.assertEqual(res, 25)
       
   def test_square_area2(self):
       res = area(0.1256)
       self.assertEqual(res, 0.01577536)

   def test_square_perimeter1(self):
       res = perimeter(5)
       self.assertEqual(res, 20)

   def test_square_perimeter2(self):
       res = perimeter(0.1384329)
       self.assertEqual(res, 0.5537316)



