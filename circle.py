import math
import unittest

def area(r):
    """
    Вычисляет площадь круга по заданному радиусу.

    Параметры:
    r (float): радиус круга

    Возвращаемое значение:
    float: площадь круга
    """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет длину окружности по заданному радиусу.

    Параметры:
    r (float): радиус окружности

    Возвращаемое значение:
    float: длина окружности
    """
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):

    # Тесты для функции area
    def test_area_positive_integer(self):
        res = area(5)
        expected = math.pi * 25
        self.assertAlmostEqual(res, expected)
       
    def test_area_large_number(self):
        res = area(100)
        expected = math.pi * 10000
        self.assertAlmostEqual(res, expected)

    def test_area_decimal_number(self):
        expected = math.pi * 12.25
        self.assertAlmostEqual(res, expected)

    def test_area_unit_value(self):
        res = area(1)
        expected = math.pi
        self.assertAlmostEqual(res, expected)

    def test_area_fractional_value(self):
        res = area(0.5)
        expected = math.pi * 0.25
        self.assertAlmostEqual(res, expected)

    def test_area_float_input(self):
        res = area(2.5)
        expected = math.pi * 6.25
        self.assertAlmostEqual(res, expected)

    def test_area_small_decimal(self):
        res = area(0.1)
        expected = math.pi * 0.01
        self.assertAlmostEqual(res, expected)

    def test_area_common_radius(self):
        res = area(10)
        expected = math.pi * 100
        self.assertAlmostEqual(res, expected)

    def test_area_medium_value(self):
        res = area(7)
        expected = math.pi * 49
        self.assertAlmostEqual(res, expected)

    def test_area_precise_decimal(self):
        res = area(1.25)
        expected = math.pi * 1.5625
        self.assertAlmostEqual(res, expected)

    def test_area_negative_numbers(self):
        with self.assertRaises(ValueError):
            res = area(-0.5)

    # Тесты для функции perimeter
    def test_perimeter_positive_integer(self):
        res = perimeter(5)
        expected = 2 * math.pi * 5
        self.assertAlmostEqual(res, expected)

    def test_perimeter_large_number(self):
        res = perimeter(100)
        expected = 2 * math.pi * 100
        self.assertAlmostEqual(res, expected)

    def test_perimeter_decimal_number(self):
        res = perimeter(3.5)
        expected = 2 * math.pi * 3.5
        self.assertAlmostEqual(res, expected)

    def test_perimeter_unit_value(self):
        res = perimeter(1)
        expected = 2 * math.pi
        self.assertAlmostEqual(res, expected)

    def test_perimeter_fractional_value(self):
        res = perimeter(0.5)
        expected = 2 * math.pi * 0.5
        self.assertAlmostEqual(res, expected)

    def test_perimeter_float_input(self):
        res = perimeter(2.5)
        expected = 2 * math.pi * 2.5
        self.assertAlmostEqual(res, expected)

    def test_perimeter_small_decimal(self):
        res = perimeter(0.1)
        expected = 2 * math.pi * 0.1
        self.assertAlmostEqual(res, expected)

    def test_perimeter_common_radius(self):
        res = perimeter(10)
        expected = 2 * math.pi * 10
        self.assertAlmostEqual(res, expected)

    def test_perimeter_medium_value(self):
        res = perimeter(7)
        expected = 2 * math.pi * 7
        self.assertAlmostEqual(res, expected)

    def test_perimeter_precise_decimal(self):
        res = perimeter(1.25)
        expected = 2 * math.pi * 1.25
        self.assertAlmostEqual(res, expected)

    def test_perimeter_negative_numbers(self):
        with self.assertRaises(ValueError):
            res = perimeter(-0.5)