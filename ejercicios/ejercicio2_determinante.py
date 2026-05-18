import random


class Matrix:
    """
    Representa una matriz cuadrada de tamaño N x N.
    """

    def __init__(self, size):
        """
        Inicializa una matriz vacía de tamaño N x N.
        """
        self.size = size
        self.data = []

    def fill_matrix(self):
        """
        Llena la matriz con números aleatorios entre 1 y 20.
        """
        self.data = []

        for _ in range(self.size):
            row = []

            for _ in range(self.size):
                number = random.randint(1, 20)
                row.append(number)

            self.data.append(row)

    def calculate_determinant(self, matrix=None):
        """
        Calcula el determinante de una matriz N x N.
        """
        if matrix is None:
            matrix = self.data

        size = len(matrix)

        if size == 1:
            return matrix[0][0]

        if size == 2:
            return (
                matrix[0][0] * matrix[1][1]
                - matrix[0][1] * matrix[1][0]
            )

        determinant = 0

        for column in range(size):
            minor = self.get_minor(matrix, 0, column)
            sign = (-1) ** column
            determinant += (
                sign
                * matrix[0][column]
                * self.calculate_determinant(minor)
            )

        return determinant

    @staticmethod
    def get_minor(matrix, row_to_remove, column_to_remove):
        """
        Obtiene la matriz menor eliminando una fila y una columna.
        """
        minor = []

        for row_index, row in enumerate(matrix):
            if row_index != row_to_remove:
                new_row = []

                for column_index, value in enumerate(row):
                    if column_index != column_to_remove:
                        new_row.append(value)

                minor.append(new_row)

        return minor

    def show_matrix(self):
        """
        Muestra la matriz en pantalla.
        """
        for row in self.data:
            print(row)


def main():
    """
    Ejecuta el programa principal.
    """
    size = int(input("Ingrese el tamaño de la matriz N x N: "))

    matrix = Matrix(size)
    matrix.fill_matrix()

    print("\nMatriz generada:")
    matrix.show_matrix()

    determinant = matrix.calculate_determinant()

    print(f"\nEl determinante de la matriz es: {determinant}")


if __name__ == "__main__":
    main()
