import random


TOTAL_PREGUNTAS = 60
PREGUNTAS_MATEMATICAS = 30
PREGUNTAS_VERBALES = 30


def generar_respuestas_correctas():
    """
    Genera las respuestas correctas del examen.
    """
    respuestas = []

    for _ in range(TOTAL_PREGUNTAS):
        respuestas.append(random.randint(1, 5))

    return respuestas


def calcular_puntaje(
    respuestas_estudiante,
    respuestas_correctas
):
    """
    Calcula el puntaje comparando respuestas.
    """
    puntaje = 0

    for i in range(len(respuestas_correctas)):
        if respuestas_estudiante[i] == respuestas_correctas[i]:
            puntaje += 1

    return puntaje


def solicitar_respuestas(cantidad, automatico=False):
    """
    Solicita o genera respuestas para el examen.

    Args:
        cantidad (int): Número de preguntas.
        automatico (bool): Si True genera respuestas aleatorias.

    Returns:
        list: Lista de respuestas (1-5).
    """
    if automatico:
        return [random.randint(1, 5) for _ in range(cantidad)]

    respuestas = []
    for i in range(cantidad):
        while True:
            try:
                respuesta = int(input(f"  Pregunta {i + 1} (1-5): "))
                if 1 <= respuesta <= 5:
                    respuestas.append(respuesta)
                    break
                print("  ⚠ Ingrese un número entre 1 y 5.")
            except ValueError:
                print("  ⚠ Entrada inválida.")
    return respuestas


def main():
    """
    Programa principal.
    """
    respuestas_correctas = generar_respuestas_correctas()
    modo = input("\n¿Modo automático para pruebas? (s/n): ").lower()
    automatico = modo == "s"

    estudiantes = []

    cantidad_estudiantes = int(
        input("Ingrese la cantidad de estudiantes: ")
    )

    suma_matematicas = 0
    suma_verbales = 0
    suma_total = 0

    mayor_puntaje = -1
    mejor_credencial = ""

    for _ in range(cantidad_estudiantes):

        credencial = input(
            "\nIngrese número de credencial: "
        )

        print("\nRespuestas examen matemáticas")
        respuestas_matematicas = solicitar_respuestas(
            PREGUNTAS_MATEMATICAS, automatico
        )

        print("\nRespuestas examen verbal")
        respuestas_verbales = solicitar_respuestas(
            PREGUNTAS_VERBALES, automatico
        )

        puntaje_matematicas = calcular_puntaje(
            respuestas_matematicas,
            respuestas_correctas[:30]
        )

        puntaje_verbales = calcular_puntaje(
            respuestas_verbales,
            respuestas_correctas[30:]
        )

        puntaje_total = (
            puntaje_matematicas
            + puntaje_verbales
        )

        estudiante = {
            "credencial": credencial,
            "matematicas": puntaje_matematicas,
            "verbales": puntaje_verbales,
            "total": puntaje_total
        }

        estudiantes.append(estudiante)

        suma_matematicas += puntaje_matematicas
        suma_verbales += puntaje_verbales
        suma_total += puntaje_total

        if puntaje_total > mayor_puntaje:
            mayor_puntaje = puntaje_total
            mejor_credencial = credencial

    promedio_matematicas = (
        suma_matematicas / cantidad_estudiantes
    )

    promedio_verbales = (
        suma_verbales / cantidad_estudiantes
    )

    promedio_total = (
        suma_total / cantidad_estudiantes
    )

    print("\nRESULTADOS")

    for estudiante in estudiantes:

        print("\nCredencial:",
              estudiante["credencial"])

        print("Puntaje matemáticas:",
              estudiante["matematicas"])

        print("Puntaje verbales:",
              estudiante["verbales"])

        print("Puntaje total:",
              estudiante["total"])

    print("\nPROMEDIOS")

    print("Promedio matemáticas:",
          promedio_matematicas)

    print("Promedio verbales:",
          promedio_verbales)

    print("Promedio total:",
          promedio_total)

    print(
        "\nESTUDIANTES CON PUNTAJE "
        "SUPERIOR O IGUAL AL PROMEDIO"
    )

    for estudiante in estudiantes:

        if estudiante["total"] >= promedio_total:

            print(
                "Credencial:",
                estudiante["credencial"],
                "- Puntaje:",
                estudiante["total"]
            )

    print("\nMEJOR ESTUDIANTE")

    print("Credencial:",
          mejor_credencial)

    print("Mayor puntaje:",
          mayor_puntaje)


if __name__ == "__main__":
    main()
