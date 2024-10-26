class Calculadora:
    def sumar(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            print("Error esperado: Los valores deben ser números.")
            return None
        return a + b

    def restar(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            print("Error esperado: Los valores deben ser números.")
            return None
        return a - b

    def multiplicar(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            print("Error esperado: Los valores deben ser números.")
            return None
        return a * b

    def dividir(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            print("Error esperado: Los valores deben ser números.")
            return None
        if b == 0:
            print("Error esperado: No se puede dividir entre cero.")
            return None
        return a / b
