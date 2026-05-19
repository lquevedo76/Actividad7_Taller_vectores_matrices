import unittest

from ejercicio4_ventas import (
    calcular_total_por_vendedor,
    calcular_total_por_anio,
    calcular_gran_total
)


class TestVentas(unittest.TestCase):
    """
    Pruebas unitarias para validar los cálculos de ventas.
    """

    def test_total_por_vendedor(self):
        ventas = [
            [100, 200, 300],
            [150, 250, 350]
        ]

        resultado = calcular_total_por_vendedor(ventas)

        self.assertEqual(resultado, [600, 750])

    def test_total_por_anio(self):
        ventas = [
            [100, 200, 300],
            [150, 250, 350]
        ]

        resultado = calcular_total_por_anio(ventas, 3)

        self.assertEqual(resultado, [250, 450, 650])

    def test_gran_total(self):
        ventas = [
            [100, 200, 300],
            [150, 250, 350]
        ]

        resultado = calcular_gran_total(ventas)

        self.assertEqual(resultado, 1350)

    def test_matriz_vacia(self):
        ventas = []

        resultado = calcular_gran_total(ventas)

        self.assertEqual(resultado, 0)


if __name__ == "__main__":
    unittest.main()
