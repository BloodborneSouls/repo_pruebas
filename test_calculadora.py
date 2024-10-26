import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_sumar(self):
        self.assertEqual(self.calc.sumar(5, 3), 8)
        if self.calc.sumar("cinco", 3) is None:
            print("Error esperado: prueba superada para sumar con valores incorrectos.")

    def test_restar(self):
        self.assertEqual(self.calc.restar(10, 5), 5)
        if self.calc.restar(10, "cinco") is None:
            print("Error esperado: prueba superada para restar con valores incorrectos.")

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(4, 3), 12)
        if self.calc.multiplicar(4, "tres") is None:
            print("Error esperado: prueba superada para multiplicar con valores incorrectos.")

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        if self.calc.dividir(10, 0) is None:
            print("Error esperado: prueba superada para división por cero.")
        if self.calc.dividir("diez", 2) is None:
            print("Error esperado: prueba superada para dividir con valores incorrectos.")

if __name__ == "__main__":
    unittest.main()
