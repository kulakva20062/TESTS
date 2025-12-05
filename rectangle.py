import unittest

def area(a, b):
    """
    Вычисляет площадь прямоугольника по заданным сторонам.

    Параметры:
    a (float): длина первой стороны прямоугольника
    b (float): длина второй(смежная) стороны прямоугольника

    Возвращаемое значение:
    float: площадь прямоугольника
    """
    return a * b


def perimeter(a, b):
    """
    Вычисляет периметр прямоугольника по заданным сторонам.

    Параметры:
    a (float): длина первой стороны прямоугольника
    b (float): длина второй(смежная) стороны прямоугольника

    Возвращаемое значение:
    float: периметр прямоугольника
    """
    return 2 * (a + b)

class RectangleTestCase(unittest.TestCase):

    # Тесты для функции area
    def test_area_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
       
    def test_area_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_positive_integers(self):
        res = area(5, 7)
        self.assertEqual(res, 35)

    def test_area_large_numbers(self):
        res = area(100, 200)
        self.assertEqual(res, 20000)

    def test_area_decimal_numbers(self):
        res = area(3.5, 2.5)
        self.assertAlmostEqual(res, 8.75)

    def test_area_float_input(self):
        res = area(2.5, 4.0)
        self.assertAlmostEqual(res, 10.0)

    def test_area_unit_values(self):
        res = area(1, 1)
        self.assertEqual(res, 1)

    def test_area_fractional_values(self):
        res = area(0.5, 0.25)
        self.assertAlmostEqual(res, 0.125)

    # Тесты для функции perimeter
    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_positive_integers(self):
        res = perimeter(5, 7)
        self.assertEqual(res, 24)

    def test_perimeter_large_numbers(self):
        res = perimeter(100, 200)
        self.assertEqual(res, 600)

    def test_perimeter_decimal_numbers(self):
        res = perimeter(3.5, 2.5)
        self.assertAlmostEqual(res, 12.0)

    def test_perimeter_float_input(self):
        res = perimeter(2.5, 4.0)
        self.assertAlmostEqual(res, 13.0)

    def test_perimeter_unit_values(self):
        res = perimeter(1, 1)
        self.assertEqual(res, 4)

    def test_perimeter_fractional_values(self):
        res = perimeter(0.5, 0.25)
        self.assertAlmostEqual(res, 1.5)

    