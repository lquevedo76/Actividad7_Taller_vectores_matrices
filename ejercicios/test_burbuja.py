import unittest

from ejercicio1_burbuja import ordenar_burbuja_descendente


class TestOrdenamientoBurbuja(unittest.TestCase):

    def test_lista_desordenada(self):
        resultado = ordenar_burbuja_descendente([5, 2, 8, 1])
        self.assertEqual(resultado, [8, 5, 2, 1])

    def test_lista_vacia(self):
        resultado = ordenar_burbuja_descendente([])
        self.assertEqual(resultado, [])


if __name__ == "__main__":
    unittest.main()
