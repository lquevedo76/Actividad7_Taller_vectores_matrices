def crear_equipo(codigo):
    """
    Crea un registro inicial para un equipo.
    """
    return {
        "codigo": codigo,
        "jugados": 0,
        "ganados": 0,
        "empatados": 0,
        "perdidos": 0,
        "goles_favor": 0,
        "goles_contra": 0,
        "puntos": 0
    }


def actualizar_partido(
    equipos,
    codigo_local,
    goles_local,
    codigo_visitante,
    goles_visitante
):
    """
    Actualiza la información de los equipos después de un partido.
    """
    equipo_local = equipos[codigo_local]
    equipo_visitante = equipos[codigo_visitante]

    equipo_local["jugados"] += 1
    equipo_visitante["jugados"] += 1

    equipo_local["goles_favor"] += goles_local
    equipo_local["goles_contra"] += goles_visitante

    equipo_visitante["goles_favor"] += goles_visitante
    equipo_visitante["goles_contra"] += goles_local

    if goles_local > goles_visitante:
        equipo_local["ganados"] += 1
        equipo_visitante["perdidos"] += 1
        equipo_local["puntos"] += 3

    elif goles_local < goles_visitante:
        equipo_visitante["ganados"] += 1
        equipo_local["perdidos"] += 1
        equipo_visitante["puntos"] += 3

    else:
        equipo_local["empatados"] += 1
        equipo_visitante["empatados"] += 1
        equipo_local["puntos"] += 1
        equipo_visitante["puntos"] += 1


def ordenar_tabla(equipos):
    """
    Ordena la tabla de clasificación por puntos de mayor a menor.
    """
    return sorted(
        equipos.values(),
        key=lambda equipo: equipo["puntos"],
        reverse=True
    )


def mostrar_tabla(tabla):
    """
    Muestra la tabla de clasificación.
    """
    print("\nTabla de clasificación")
    print("Código | PJ | PG | PE | PP | GF | GC | PTS")

    for equipo in tabla:
        print(
            equipo["codigo"],
            "|",
            equipo["jugados"],
            "|",
            equipo["ganados"],
            "|",
            equipo["empatados"],
            "|",
            equipo["perdidos"],
            "|",
            equipo["goles_favor"],
            "|",
            equipo["goles_contra"],
            "|",
            equipo["puntos"]
        )


def main():
    """
    Ejecuta el programa principal.
    """
    equipos = {}

    cantidad_equipos = int(input("Ingrese la cantidad de equipos: "))

    for i in range(cantidad_equipos):
        codigo = input(f"Ingrese el código del equipo {i + 1}: ")
        equipos[codigo] = crear_equipo(codigo)

    cantidad_partidos = int(input("\nIngrese la cantidad de partidos: "))

    for i in range(cantidad_partidos):
        print(f"\nPartido {i + 1}")

        codigo_local = input("Código equipo local: ")
        goles_local = int(input("Goles equipo local: "))

        codigo_visitante = input("Código equipo visitante: ")
        goles_visitante = int(input("Goles equipo visitante: "))

        actualizar_partido(
            equipos,
            codigo_local,
            goles_local,
            codigo_visitante,
            goles_visitante
        )

    tabla_ordenada = ordenar_tabla(equipos)
    mostrar_tabla(tabla_ordenada)


if __name__ == "__main__":
    main()
