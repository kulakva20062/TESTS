import unittest

def area(a):
    """
    Вычисляет площадь квадрата по заданной длине стороны.

    Параметры:
    a (float): длина стороны квадрата

    Возвращаемое значение:
    float: площадь квадрата
    """
    return a * a


def perimeter(a):
    """
    Вычисляет периметр квадрата по заданной длине стороны.

    Параметры:
    a (float): длина стороны квадрата

    Возвращаемое значение:
    float: периметр квадрата
    """
    return 4 * a


class SquareTestCase(unittest.TestCase):
    
    # Тесты для функции area
    def test_area_positive_integer(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_large_number(self):
        res = area(100)
        self.assertEqual(res, 10000)

    def test_area_decimal_number(self):
        res = area(3.5)
        self.assertAlmostEqual(res, 12.25)

    def test_area_unit_value(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_area_fractional_value(self):
        res = area(0.5)
        self.assertAlmostEqual(res, 0.25)

    def test_area_float_input(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25)

    def test_area_small_decimal(self):
        res = area(0.1)
        self.assertAlmostEqual(res, 0.01)

    # Тесты для функции perimeter
    def test_perimeter_positive_integer(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_large_number(self):
        res = perimeter(100)
        self.assertEqual(res, 400)

    def test_perimeter_decimal_number(self):
        res = perimeter(3.5)
        self.assertAlmostEqual(res, 14.0)

    def test_perimeter_unit_value(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_perimeter_fractional_value(self):
        res = perimeter(0.5)
        self.assertAlmostEqual(res, 2.0)

    def test_perimeter_float_input(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 10.0)

    def test_perimeter_small_decimal(self):
        res = perimeter(0.1)
        self.assertAlmostEqual(res, 0.4)
