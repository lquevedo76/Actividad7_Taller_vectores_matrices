import unittest

from ejercicio3_admision import calcular_puntaje


class TestAdmision(unittest.TestCase):
    """
    Pruebas unitarias para validar el cálculo de puntajes
    del examen de admisión.
    """

    def test_todas_las_respuestas_correctas(self):
        respuestas_estudiante = [1, 2, 3, 4, 5]
        respuestas_correctas = [1, 2, 3, 4, 5]

        resultado = calcular_puntaje(
            respuestas_estudiante,
            respuestas_correctas
        )

        self.assertEqual(resultado, 5)

    def test_todas_las_respuestas_incorrectas(self):
        respuestas_estudiante = [1, 1, 1, 1, 1]
        respuestas_correctas = [2, 2, 2, 2, 2]

        resultado = calcular_puntaje(
            respuestas_estudiante,
            respuestas_correctas
        )

        self.assertEqual(resultado, 0)

    def test_algunas_respuestas_correctas(self):
        respuestas_estudiante = [1, 2, 3, 4, 5]
        respuestas_correctas = [1, 4, 3, 2, 5]

        resultado = calcular_puntaje(
            respuestas_estudiante,
            respuestas_correctas
        )

        self.assertEqual(resultado, 3)

    def test_lista_vacia(self):
        respuestas_estudiante = []
        respuestas_correctas = []

        resultado = calcular_puntaje(
            respuestas_estudiante,
            respuestas_correctas
        )

        self.assertEqual(resultado, 0)


if __name__ == "__main__":
    unittest.main()
