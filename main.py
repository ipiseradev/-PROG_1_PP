
import biblioteca as bib


def mostrar_menu():
        """Muestra el menú de opciones por consola."""
        print("\n========== MENÚ DE OPCIONES ==========")
        print("1 - Cargar datos de los estudiantes")
        print("2 - Mostrar todos los estudiantes")
        print("3 - Calcular promedios")
        print("4 - Mostrar estudiantes ordenados por promedio (DESC)")
        print("5 - Mostrar estudiante/s con mayor promedio")
        print("6 - Buscar estudiante por legajo")
        print("7 - Salir")
        print("======================================")


def opcion_cargar(legajos, nombres, generos, parciales1, parciales2, promedios):
        """
        Ítem 1: carga los datos, de forma manual o con datos de prueba.

        Retorna:
            bool: True cuando los datos quedaron cargados.
        """
        print("\na - Carga manual por consola")
        print("b - Cargar datos de prueba (hardcodeados)")
        modo = input("Elija el modo de carga: ").strip().lower()
        while modo not in ("a", "b"):
            modo = input("Opción inválida. Elija 'a' o 'b': ").strip().lower()

        if modo == "a":
            bib.cargar_datos(legajos, nombres, generos, parciales1, parciales2)
        else:
            bib.cargar_datos_prueba(legajos, nombres, generos, parciales1, parciales2)

        promedios.clear()  # si se recargan datos, los promedios anteriores no sirven
        print("\nDatos cargados correctamente.")
        return True


def opcion_mostrar(legajos, nombres, generos, parciales1, parciales2):
        """Ítem 2: muestra el informe con todos los estudiantes."""
        bib.mostrar_estudiantes("Listado de estudiantes",
                                legajos, nombres, generos, parciales1, parciales2)


def opcion_calcular_promedios(legajos, nombres, generos, parciales1, parciales2, promedios):
        """Ítem 3: calcula el promedio de cada estudiante y lo guarda en la lista de promedios."""
        bib.calcular_promedios(parciales1, parciales2, promedios)
        print("\nPromedios calculados correctamente.")
        bib.mostrar_estudiantes("Promedios de estudiantes",
                                legajos, nombres, generos, parciales1, parciales2, promedios)


def asegurar_promedios(parciales1, parciales2, promedios):
        """Calcula los promedios si todavía no fueron calculados."""
        if len(promedios) != len(parciales1):
            bib.calcular_promedios(parciales1, parciales2, promedios)


def opcion_ordenar(legajos, nombres, generos, parciales1, parciales2, promedios):
        """
        Ítem 4: muestra los estudiantes ordenados por promedio de forma DESC.
        Se ordenan copias para no alterar el orden original de las listas.
        """
        asegurar_promedios(parciales1, parciales2, promedios)

        copias = [legajos[:], nombres[:], generos[:], parciales1[:], parciales2[:], promedios[:]]
        bib.ordenar(copias, 5, "DESC")

        bib.mostrar_estudiantes("Estudiantes ordenados por promedio (DESC)",
                                copias[0], copias[1], copias[2], copias[3], copias[4], copias[5])


def opcion_mayor_promedio(legajos, nombres, generos, parciales1, parciales2, promedios):
        """Ítem 5: muestra el/los estudiante/s con mayor promedio."""
        asegurar_promedios(parciales1, parciales2, promedios)
        indices = bib.buscar_mayor_promedio(promedios)
        bib.mostrar_estudiantes("Estudiante/s con mayor promedio",
                                legajos, nombres, generos, parciales1, parciales2,
                                promedios, indices)


def opcion_buscar(legajos, nombres, generos, parciales1, parciales2, promedios):
        """Ítem 6: busca un estudiante por legajo y muestra todos sus datos."""
        texto = input("\nIngrese el legajo a buscar: ").strip()
        while not texto.isdigit():
            texto = input("Error: ingrese un legajo numérico: ").strip()

        posicion = bib.buscar_legajo(legajos, int(texto))
        if posicion == -1:
            print("No se encontró ningún estudiante con ese legajo.")
            return

        proms = promedios if len(promedios) == len(legajos) else None
        bib.mostrar_estudiantes("Datos del estudiante",
                                legajos, nombres, generos, parciales1, parciales2,
                                proms, [posicion])


def main():
        """Función principal: maneja el menú y la validación de datos cargados."""
        legajos = []
        nombres = []
        generos = []
        parciales1 = []
        parciales2 = []
        promedios = []
        datos_cargados = False

        while True:
            mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "7":
                print("\nSaliendo del programa. ¡Hasta luego!")
                break
            elif opcion == "1":
                datos_cargados = opcion_cargar(legajos, nombres, generos,
                                            parciales1, parciales2, promedios)
            elif opcion in ("2", "3", "4", "5", "6"):
                if not datos_cargados:
                    print("\nError: primero debe cargar los datos (opción 1).")
                    continue
                if opcion == "2":
                    opcion_mostrar(legajos, nombres, generos, parciales1, parciales2)
                elif opcion == "3":
                    opcion_calcular_promedios(legajos, nombres, generos,
                                            parciales1, parciales2, promedios)
                elif opcion == "4":
                    opcion_ordenar(legajos, nombres, generos,
                                parciales1, parciales2, promedios)
                elif opcion == "5":
                    opcion_mayor_promedio(legajos, nombres, generos,
                                        parciales1, parciales2, promedios)
                elif opcion == "6":
                    opcion_buscar(legajos, nombres, generos,
                                parciales1, parciales2, promedios)
            else:
                print("\nOpción inválida. Ingrese un número del 1 al 7.")


if __name__ == "__main__":
        main()