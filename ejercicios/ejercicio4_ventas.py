def solicitar_ventas(cantidad_vendedores, cantidad_anios):
    """
    Solicita las ventas de cada vendedor por cada año.
    """
    ventas = []

    for vendedor in range(cantidad_vendedores):
        fila_ventas = []

        print(f"\nVendedor {vendedor + 1}")

        for anio in range(cantidad_anios):
            venta = float(
                input(f"Ingrese ventas del año {anio + 1}: ")
            )
            fila_ventas.append(venta)

        ventas.append(fila_ventas)

    return ventas


def calcular_total_por_vendedor(ventas):
    """
    Calcula el total de ventas de cada vendedor.
    """
    totales_vendedores = []

    for fila in ventas:
        total = sum(fila)
        totales_vendedores.append(total)

    return totales_vendedores


def calcular_total_por_anio(ventas, cantidad_anios):
    """
    Calcula el total de ventas por cada año.
    """
    totales_anios = []

    for anio in range(cantidad_anios):
        total = 0

        for fila in ventas:
            total += fila[anio]

        totales_anios.append(total)

    return totales_anios


def calcular_gran_total(ventas):
    """
    Calcula el total general de ventas de la empresa.
    """
    gran_total = 0

    for fila in ventas:
        gran_total += sum(fila)

    return gran_total


def mostrar_matriz(ventas):
    """
    Muestra la matriz de ventas.
    """
    print("\nMatriz de ventas:")

    for fila in ventas:
        print(fila)


def main():
    """
    Ejecuta el programa principal.
    """
    cantidad_vendedores = int(
        input("Ingrese la cantidad de vendedores: ")
    )

    cantidad_anios = int(
        input("Ingrese la cantidad de años: ")
    )

    ventas = solicitar_ventas(cantidad_vendedores, cantidad_anios)

    total_vendedores = calcular_total_por_vendedor(ventas)
    total_anios = calcular_total_por_anio(ventas, cantidad_anios)
    gran_total = calcular_gran_total(ventas)

    mostrar_matriz(ventas)

    print("\nTotal de ventas por vendedor:")
    for i, total in enumerate(total_vendedores):
        print(f"Vendedor {i + 1}: {total}")

    print("\nTotal de ventas por año:")
    for i, total in enumerate(total_anios):
        print(f"Año {i + 1}: {total}")

    print(f"\nGran total de ventas de la empresa: {gran_total}")


if __name__ == "__main__":
    main()
