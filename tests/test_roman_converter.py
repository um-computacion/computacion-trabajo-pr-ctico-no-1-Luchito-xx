import unittest
from src.roman_converter import decimal_to_roman 


class TestRomanConverter(unittest.TestCase):
    def test_basicos(self):
        self.assertEqual(decimal_to_roman(1), 'I')
        self.assertEqual(decimal_to_roman(5), 'V')
        self.assertEqual(decimal_to_roman(10), 'X')
        self.assertEqual(decimal_to_roman(50), 'L')
        self.assertEqual(decimal_to_roman(100), 'C')
        self.assertEqual(decimal_to_roman(500), 'D')
        self.assertEqual(decimal_to_roman(1000), 'M')

    def test_sustracciones(self):
        self.assertEqual(decimal_to_roman(4), 'IV')
        self.assertEqual(decimal_to_roman(9), 'IX')
        self.assertEqual(decimal_to_roman(40), 'XL')
        self.assertEqual(decimal_to_roman(90), 'XC')
        self.assertEqual(decimal_to_roman(400), 'CD')
        self.assertEqual(decimal_to_roman(900), 'CM')

    def test_numeros_compuestos(self):
        self.assertEqual(decimal_to_roman(999), 'CMXCIX')
        self.assertEqual(decimal_to_roman(666), 'DCLXVI')
        self.assertEqual(decimal_to_roman(333), 'CCCXXXIII')

    def test_limites(self):
        with self.assertRaises(ValueError):
            decimal_to_roman(0)
        with self.assertRaises(ValueError):
            decimal_to_roman(4000)

if __name__ == '__main__':
    unittest.main()
