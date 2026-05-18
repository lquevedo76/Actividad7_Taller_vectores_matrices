import unittest

from ejercicio2_determinante import Matrix


class TestMatrix(unittest.TestCase):
    """
    Pruebas unitarias para validar la clase Matrix.
    """

    def test_determinant_1x1(self):
        matrix = Matrix(1)
        matrix.data = [[5]]

        result = matrix.calculate_determinant()

        self.assertEqual(result, 5)

    def test_determinant_2x2(self):
        matrix = Matrix(2)
        matrix.data = [
            [3, 2],
            [5, 4]
        ]

        result = matrix.calculate_determinant()

        self.assertEqual(result, 2)

    def test_determinant_3x3(self):
        matrix = Matrix(3)
        matrix.data = [
            [6, 1, 1],
            [4, -2, 5],
            [2, 8, 7]
        ]

        result = matrix.calculate_determinant()

        self.assertEqual(result, -306)

    def test_fill_matrix_size(self):
        matrix = Matrix(3)
        matrix.fill_matrix()

        self.assertEqual(len(matrix.data), 3)

        for row in matrix.data:
            self.assertEqual(len(row), 3)

    def test_fill_matrix_values_between_1_and_20(self):
        matrix = Matrix(3)
        matrix.fill_matrix()

        for row in matrix.data:
            for value in row:
                self.assertGreaterEqual(value, 1)
                self.assertLessEqual(value, 20)


if __name__ == "__main__":
    unittest.main()
