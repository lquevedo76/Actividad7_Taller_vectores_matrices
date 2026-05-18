def ordenar_burbuja_descendente(arreglo):
    """
    Ordena un arreglo de mayor a menor usando el método burbuja.
    """
    longitud = len(arreglo)

    for i in range(longitud):
        for j in range(0, longitud - i - 1):
            if arreglo[j] < arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

    return arreglo


def solicitar_numeros():
    """
    Solicita al usuario los números del arreglo.
    """
    cantidad = int(input("Ingrese la cantidad de elementos: "))
    numeros = []

    for i in range(cantidad):
        numero = int(input(f"Ingrese el elemento {i + 1}: "))
        numeros.append(numero)

    return numeros


def main():
    """
    Ejecuta el programa principal.
    """
    arreglo = solicitar_numeros()

    print("\nArreglo original:")
    print(arreglo)

    arreglo_ordenado = ordenar_burbuja_descendente(arreglo.copy())

    print("\nArreglo ordenado de mayor a menor:")
    print(arreglo_ordenado)


if __name__ == "__main__":
    main()
