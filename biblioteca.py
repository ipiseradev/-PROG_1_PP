"""
biblioteca.py
Biblioteca de funciones propias para procesar los datos de estudiantes
de una institución educativa, trabajando con listas paralelas.
"""

CANTIDAD_ESTUDIANTES = 30
GENEROS_VALIDOS = ['F', 'M', 'X']
NOTA_MINIMA = 1
NOTA_MAXIMA = 10



# VALIDACIONES (una función por cada dato)


def validar_legajo(texto, legajos):
    """
    Valida que el legajo sea un número entero positivo y que no esté repetido.

    Parámetros:
        texto (str): valor ingresado por el usuario.
        legajos (list): legajos ya cargados.
    Retorna:
        bool: True si es válido, False en caso contrario.
    """
    if not texto.isdigit():
        return False
    legajo = int(texto)
    if legajo <= 0:
        return False
    if legajo in legajos:
        return False
    return True


def validar_nombre(texto):
    """
    Valida que el apellido y nombre contenga solo letras (se permiten espacios).

    Parámetros:
        texto (str): valor ingresado por el usuario.
    Retorna:
        bool: True si es alfabético, False en caso contrario.
    """
    texto = texto.strip()
    if texto == "":
        return False
    return texto.replace(" ", "").isalpha()


def validar_genero(texto):
    """
    Valida que el género sea 'F', 'M' o 'X'.

    Parámetros:
        texto (str): valor ingresado por el usuario.
    Retorna:
        bool: True si es un género válido, False en caso contrario.
    """
    return texto.strip().upper() in GENEROS_VALIDOS


def validar_nota(texto):
    """
    Valida que la nota sea un número entero entre 1 y 10.

    Parámetros:
        texto (str): valor ingresado por el usuario.
    Retorna:
        bool: True si es una nota válida, False en caso contrario.
    """
    texto = texto.strip()
    if not texto.isdigit():
        return False
    nota = int(texto)
    return NOTA_MINIMA <= nota <= NOTA_MAXIMA



# CARGA DE DATOS (una función por cada dato)


def pedir_legajo(legajos):
    """
    Solicita un legajo por consola hasta que sea válido.

    Parámetros:
        legajos (list): legajos ya cargados (para evitar repetidos).
    Retorna:
        int: legajo válido.
    """
    texto = input("Legajo: ")
    while not validar_legajo(texto, legajos):
        print("  Error: el legajo debe ser un entero positivo y no repetido.")
        texto = input("Legajo: ")
    return int(texto)


def pedir_nombre():
    """
    Solicita el apellido y nombre por consola hasta que sea válido.

    Retorna:
        str: apellido y nombre con formato título.
    """
    texto = input("Apellido y nombre: ")
    while not validar_nombre(texto):
        print("  Error: solo se permiten letras y espacios.")
        texto = input("Apellido y nombre: ")
    return texto.strip().title()


def pedir_genero():
    """
    Solicita el género por consola hasta que sea válido.

    Retorna:
        str: género en mayúscula ('F', 'M' o 'X').
    """
    texto = input("Género (F/M/X): ")
    while not validar_genero(texto):
        print("  Error: el género debe ser F, M o X.")
        texto = input("Género (F/M/X): ")
    return texto.strip().upper()


def pedir_nota(numero_parcial):
    """
    Solicita la nota de un parcial por consola hasta que sea válida.

    Parámetros:
        numero_parcial (int): número de parcial (1 o 2), usado en el mensaje.
    Retorna:
        int: nota válida entre 1 y 10.
    """
    mensaje = f"Nota del parcial {numero_parcial} (1-10): "
    texto = input(mensaje)
    while not validar_nota(texto):
        print("  Error: la nota debe ser un entero entre 1 y 10.")
        texto = input(mensaje)
    return int(texto)


def cargar_datos(legajos, nombres, generos, parciales1, parciales2):
    """
    Carga por consola los datos de todos los estudiantes en las listas paralelas.
    Vacía las listas antes de cargar.

    Parámetros:
        legajos, nombres, generos, parciales1, parciales2 (list): listas paralelas a cargar.
    """
    for lista in (legajos, nombres, generos, parciales1, parciales2):
        lista.clear()

    for i in range(CANTIDAD_ESTUDIANTES):
        print(f"\n--- Estudiante {i + 1} de {CANTIDAD_ESTUDIANTES} ---")
        legajos.append(pedir_legajo(legajos))
        nombres.append(pedir_nombre())
        generos.append(pedir_genero())
        parciales1.append(pedir_nota(1))
        parciales2.append(pedir_nota(2))


def cargar_datos_prueba(legajos, nombres, generos, parciales1, parciales2):
    """
    Carga datos hardcodeados de 30 estudiantes para pruebas de funcionamiento.
    Vacía las listas antes de cargar.

    Parámetros:
        legajos, nombres, generos, parciales1, parciales2 (list): listas paralelas a cargar.
    """
    for lista in (legajos, nombres, generos, parciales1, parciales2):
        lista.clear()

    legajos.extend(list(range(1001, 1031)))
    nombres.extend([
        "Gomez Juan", "Perez Maria", "Lopez Carlos", "Fernandez Ana", "Martinez Lucas",
        "Rodriguez Sofia", "Sanchez Diego", "Romero Valentina", "Diaz Mateo", "Alvarez Camila",
        "Torres Nicolas", "Ruiz Martina", "Ramirez Tomas", "Flores Lucia", "Acosta Joaquin",
        "Benitez Julieta", "Medina Franco", "Herrera Agustina", "Suarez Bruno", "Aguirre Paula",
        "Gimenez Santiago", "Molina Florencia", "Castro Ignacio", "Ortiz Milagros", "Silva Facundo",
        "Rojas Abril", "Nuñez Thiago", "Luna Morena", "Juarez Benjamin", "Cabrera Delfina"
    ])
    generos.extend([
        "M", "F", "M", "F", "M", "F", "M", "F", "M", "F",
        "M", "F", "X", "F", "M", "F", "M", "F", "M", "F",
        "M", "F", "M", "X", "M", "F", "M", "F", "M", "F"
    ])
    parciales1.extend([7, 8, 5, 10, 6, 9, 4, 7, 8, 3,
            6, 9, 7, 5, 8, 10, 2, 6, 7, 9,
            5, 8, 6, 4, 9, 7, 10, 6, 8, 5])
    parciales2.extend([8, 6, 7, 9, 5, 10, 6, 8, 7, 4,
            7, 8, 9, 6, 6, 9, 3, 7, 8, 8,
            6, 9, 5, 7, 10, 8, 9, 5, 7, 6])


# MOSTRAR (una función que recorre y otra que muestra un elemento)


def mostrar_estudiante(legajo, nombre, genero, parcial1, parcial2, promedio=None):
    """
    Muestra los datos de un único estudiante en formato de fila de informe.

    Parámetros:
        legajo (int), nombre (str), genero (str), parcial1 (int), parcial2 (int).
        promedio (float, opcional): si se informa, se muestra con 2 decimales.
    """
    fila = f"{legajo:<8}{nombre:<25}{genero:^8}{parcial1:^10}{parcial2:^10}"
    if promedio is not None:
        fila += f"{promedio:^10.2f}"
    print(fila)


def mostrar_estudiantes(titulo, legajos, nombres, generos, parciales1, parciales2,
                        promedios=None, indices=None):
    """
    Recorre las listas paralelas y muestra un informe con título y registros.
    Llama a mostrar_estudiante() por cada elemento.

    Parámetros:
        titulo (str): título del informe.
        legajos, nombres, generos, parciales1, parciales2 (list): listas paralelas.
        promedios (list, opcional): si se informa, se agrega la columna promedio.
        indices (list, opcional): posiciones a mostrar. Si es None, se muestran todas.
    """
    if indices is None:
        indices = range(len(legajos))

    ancho = 71 if promedios is not None else 61
    print("\n" + "=" * ancho)
    print(titulo.upper().center(ancho))
    print("=" * ancho)

    encabezado = f"{'Legajo':<8}{'Apellido y nombre':<25}{'Género':^8}{'Parcial 1':^10}{'Parcial 2':^10}"
    if promedios is not None:
        encabezado += f"{'Promedio':^10}"
    print(encabezado)
    print("-" * ancho)

    for i in indices:
        promedio = promedios[i] if promedios is not None else None
        mostrar_estudiante(legajos[i], nombres[i], generos[i],
            parciales1[i], parciales2[i], promedio)

    print("=" * ancho)



# PROMEDIOS


def calcular_promedio(nota1, nota2):
    """
    Calcula el promedio de dos notas.

    Parámetros:
        nota1 (int), nota2 (int): notas entre 1 y 10.
    Retorna:
        float: promedio entre 1.00 y 10.00 redondeado a 2 decimales.
    """
    return round((nota1 + nota2) / 2, 2)


def calcular_promedios(parciales1, parciales2, promedios):
    """
    Calcula el promedio de cada estudiante y lo guarda en la lista de promedios.
    Vacía la lista de promedios antes de calcular.

    Parámetros:
        parciales1, parciales2 (list): notas de cada parcial.
        promedios (list): lista donde se guardan los promedios.
    """
    promedios.clear()
    for i in range(len(parciales1)):
        promedios.append(calcular_promedio(parciales1[i], parciales2[i]))



# ORDENAMIENTO Y BÚSQUEDAS


def ordenar(listas, indice_clave, orden="ASC"):
    """
    Ordena listas paralelas según una de ellas (método burbuja).
    Al intercambiar, se intercambian los elementos de TODAS las listas
    para mantener la correspondencia.

    Parámetros:
        listas (list): lista de listas paralelas a ordenar.
        indice_clave (int): posición, dentro de 'listas', de la lista usada como criterio.
        orden (str): "ASC" para ascendente o "DESC" para descendente.
    """
    clave = listas[indice_clave]
    n = len(clave)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if orden == "ASC":
                intercambiar = clave[j] > clave[j + 1]
            else:
                intercambiar = clave[j] < clave[j + 1]
            if intercambiar:
                for lista in listas:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]


def buscar_mayor_promedio(promedios):
    """
    Busca la/s posición/es con el mayor promedio.

    Parámetros:
        promedios (list): lista de promedios.
    Retorna:
        list: índices de los estudiantes con el mayor promedio.
    """
    maximo = promedios[0]
    for promedio in promedios:
        if promedio > maximo:
            maximo = promedio

    indices = []
    for i in range(len(promedios)):
        if promedios[i] == maximo:
            indices.append(i)
    return indices


def buscar_legajo(legajos, legajo):
    """
    Busca la posición de un legajo en la lista.

    Parámetros:
        legajos (list): lista de legajos.
        legajo (int): legajo a buscar.
    Retorna:
        int: posición del legajo, o -1 si no existe.
    """
    for i in range(len(legajos)):
        if legajos[i] == legajo:
            return i
    return -1