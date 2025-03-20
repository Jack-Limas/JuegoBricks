# test_calculadora.py
import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        """ Configuración antes de cada test """
        self.calc = Calculadora()

    def test_suma(self):
        self.assertEqual(self.calc.suma(2, 3), 5)
        self.assertEqual(self.calc.suma(-1, 1), 0)

    def test_resta(self):
        self.assertEqual(self.calc.resta(10, 4), 6)

    def test_division(self):
        self.assertEqual(self.calc.division(10, 2), 5)

        # Prueba de error (División por cero)
        with self.assertRaises(ValueError):
            self.calc.division(5, 0)

if __name__ == '__main__':
    unittest.main()