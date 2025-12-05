import unittest

def area(a, h):
    """
    Вычисляет площадь треугольника по основанию и высоте.

    Параметры:
    a (float): длина основания треугольника
    h (float): высота треугольника, проведенная к основанию

    Возвращаемое значение:
    float: площадь треугольника
    """
    return a * h / 2


def perimeter(a, b, c):
    """
    Вычисляет периметр треугольника по длинам трех сторон.

    Параметры:
    a (float): длина первой стороны треугольника
    b (float): длина второй стороны треугольника
    c (float): длина третьей стороны треугольника

    Возвращаемое значение:
    float: периметр треугольника
    """
    return a + b + c

class TriangleTestCase(unittest.TestCase):

    # Тесты для функции area
    def test_area_positive_integers(self):
        res = area(6, 4)
        self.assertEqual(res, 12)

    def test_area_large_numbers(self):
        res = area(100, 50)
        self.assertEqual(res, 2500)

    def test_area_decimal_numbers(self):
        res = area(5.5, 3.2)
        self.assertAlmostEqual(res, 8.8)

    def test_area_unit_values(self):
        res = area(1, 1)
        self.assertEqual(res, 0.5)

    def test_area_fractional_values(self):
        res = area(0.5, 0.4)
        self.assertAlmostEqual(res, 0.1)

    def test_area_float_input(self):
        res = area(3.0, 2.5)
        self.assertAlmostEqual(res, 3.75)

    def test_area_small_decimals(self):
        res = area(0.2, 0.3)
        self.assertAlmostEqual(res, 0.03)

    def test_area_common_values(self):
        res = area(10, 8)
        self.assertEqual(res, 40)

    def test_area_medium_values(self):
        res = area(7, 6)
        self.assertEqual(res, 21)

    def test_area_precise_decimals(self):
        res = area(2.5, 1.6)
        self.assertAlmostEqual(res, 2.0)

    def test_area_negative_numbers(self):
        with self.assertRaises(ValueError):
            res = area(-2.5, -1.6)

    # Тесты для функции perimeter
    def test_perimeter_positive_integers(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_large_numbers(self):
        res = perimeter(100, 150, 200)
        self.assertEqual(res, 450)

    def test_perimeter_decimal_numbers(self):
        res = perimeter(3.5, 4.2, 5.7)
        self.assertAlmostEqual(res, 13.4)

    def test_perimeter_unit_values(self):
        res = perimeter(1, 1, 1)
        self.assertEqual(res, 3)

    def test_perimeter_fractional_values(self):
        res = perimeter(0.5, 0.6, 0.7)
        self.assertAlmostEqual(res, 1.8)

    def test_perimeter_float_input(self):
        res = perimeter(2.5, 3.0, 4.5)
        self.assertAlmostEqual(res, 10.0)

    def test_perimeter_small_decimals(self):
        res = perimeter(0.1, 0.2, 0.3)
        self.assertAlmostEqual(res, 0.6)

    def test_perimeter_common_values(self):
        res = perimeter(5, 12, 13)
        self.assertEqual(res, 30)

    def test_perimeter_medium_values(self):
        res = perimeter(7, 8, 9)
        self.assertEqual(res, 24)

    def test_perimeter_precise_decimals(self):
        res = perimeter(1.25, 2.75, 3.5)
        self.assertAlmostEqual(res, 7.5)

    def test_perimeter_negative_numbers(self):
        with self.assertRaises(ValueError):
            res = perimeter(-2.5, -1.6, -100)

    