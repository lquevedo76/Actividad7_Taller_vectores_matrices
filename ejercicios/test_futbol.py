import unittest

from ejercicio5_futbol import (
    crear_equipo,
    actualizar_partido,
    ordenar_tabla
)


class TestFutbol(unittest.TestCase):
    """
    Pruebas unitarias para validar la tabla de clasificación.
    """

    def test_equipo_local_gana(self):
        equipos = {
            "A": crear_equipo("A"),
            "B": crear_equipo("B")
        }

        actualizar_partido(equipos, "A", 2, "B", 1)

        self.assertEqual(equipos["A"]["puntos"], 3)
        self.assertEqual(equipos["A"]["ganados"], 1)
        self.assertEqual(equipos["B"]["perdidos"], 1)

    def test_equipo_visitante_gana(self):
        equipos = {
            "A": crear_equipo("A"),
            "B": crear_equipo("B")
        }

        actualizar_partido(equipos, "A", 0, "B", 2)

        self.assertEqual(equipos["B"]["puntos"], 3)
        self.assertEqual(equipos["B"]["ganados"], 1)
        self.assertEqual(equipos["A"]["perdidos"], 1)

    def test_partido_empatado(self):
        equipos = {
            "A": crear_equipo("A"),
            "B": crear_equipo("B")
        }

        actualizar_partido(equipos, "A", 1, "B", 1)

        self.assertEqual(equipos["A"]["puntos"], 1)
        self.assertEqual(equipos["B"]["puntos"], 1)
        self.assertEqual(equipos["A"]["empatados"], 1)
        self.assertEqual(equipos["B"]["empatados"], 1)

    def test_ordenar_tabla(self):
        equipos = {
            "A": crear_equipo("A"),
            "B": crear_equipo("B")
        }

        actualizar_partido(equipos, "A", 3, "B", 1)

        tabla = ordenar_tabla(equipos)

        self.assertEqual(tabla[0]["codigo"], "A")


if __name__ == "__main__":
    unittest.main()
