import Planeta
import Nave
import Personaje
import json
import os

class Mision:
    """
    Clase que representa una misión en el contexto de un juego o simulación.
    Una misión incluye un nombre, un planeta destino, una nave, armas y personajes participantes.

    Atributos:
        nombre (str): Nombre de la misión.
        planeta_destino (Planeta): Objeto que representa el planeta destino de la misión.
        nave (Nave): Objeto que representa la nave utilizada en la misión.
        armas (list): Lista de nombres de armas utilizadas en la misión.
        integrantes (list): Lista de objetos Personaje que participan en la misión.
    """

    def __init__(self, nombre, planeta_destino, nave, armas, integrantes):
        """
        Inicializa una nueva misión con los detalles proporcionados.

        Args:
            nombre (str): Nombre de la misión.
            planeta_destino (Planeta): El planeta destino de la misión.
            nave (Nave): La nave que se utilizará en la misión.
            armas (list): Una lista de nombres (strings) de las armas que se usarán en la misión.
            integrantes (list): Una lista de objetos Personaje que participarán en la misión.
        """
        self.nombre = nombre
        self.planeta_destino = planeta_destino
        self.nave = nave
        self.armas = armas
        self.integrantes = integrantes

    def __str__(self):
        """
        Retorna una cadena de texto que representa la misión con sus atributos formateados.

        Returns:
            str: Una descripción legible de la misión que incluye el nombre, el planeta destino, 
                 la nave utilizada, las armas y los personajes que participan.
        """
        return (f'Misión: {self.nombre}\n'
                f'Planeta Destino: {self.planeta_destino.nombre}\n'
                f'Nave: {self.nave.nombre}\n'
                f'Armas: {", ".join(self.armas)}\n'
                f'Integrantes: {", ".join([integrante.nombre for integrante in self.integrantes])}\n')

def guardar_misiones(misiones, usuario):
    """
    Guarda las misiones asociadas a un usuario específico en un archivo de texto.

    El archivo es nombrado según el usuario, y cada línea del archivo representa una misión con
    los detalles esenciales separados por comas.

    Args:
        misiones (list): Lista de objetos Mision que deben ser guardados.
        usuario (str): El nombre del usuario cuyas misiones se están guardando.
    
    Detalles guardados:
        - Nombre de la misión
        - ID del planeta destino
        - ID de la nave utilizada
        - Nombres de las armas (separados por '|')
        - IDs de los personajes participantes (separados por '|')
    """
    archivo_misiones = f'misiones_{usuario}.txt'  # El archivo se asocia con el nombre del usuario
    with open(archivo_misiones, 'w') as file:
        for mision in misiones:
            mision_data = {
                'nombre_mision': mision.nombre,
                'numero_planeta': mision.planeta_destino.id,  # ID único del planeta destino
                'numero_nave': mision.nave.id,  # ID único de la nave utilizada
                'armas': mision.armas,  # Lista de nombres de armas utilizadas
                'numero_integrantes': [integrante.id for integrante in mision.integrantes]  # Lista de IDs de los personajes participantes
            }
            # Escribir los datos de la misión en el archivo de texto
            file.write(f"{usuario},{mision_data['nombre_mision']},{mision_data['numero_planeta']},{mision_data['numero_nave']},{'|'.join(mision_data['armas'])},{'|'.join(map(str, mision_data['numero_integrantes']))}\n")

def cargar_misiones(usuario, planetas, naves, personajes):
    """
    Carga las misiones asociadas a un usuario desde un archivo de texto.

    Cada misión es reconstruida usando los objetos correspondientes de Planeta, Nave y Personaje,
    según los IDs almacenados en el archivo de texto.

    Args:
        usuario (str): El nombre del usuario cuyas misiones se desean cargar.
        planetas (list): Lista de objetos Planeta disponibles.
        naves (list): Lista de objetos Nave disponibles.
        personajes (list): Lista de objetos Personaje disponibles.

    Returns:
        list: Una lista de objetos Mision que pertenecen al usuario.
    
    Proceso:
        - Se verifica la existencia del archivo de misiones asociado al usuario.
        - Se lee cada línea del archivo y se separan los valores para reconstruir las misiones.
        - Se busca el objeto Planeta, Nave y Personaje correspondiente a cada ID almacenado.
        - Las misiones se reconstruyen y se agregan a una lista que es retornada.
    """
    archivo_misiones = f'misiones_{usuario}.txt'
    misiones = []

    if not os.path.exists(archivo_misiones):
        print(f"No se encontraron misiones para el usuario {usuario}.")
        return misiones

    with open(archivo_misiones, 'r') as file:
        for linea in file:
            # Separamos los valores en la línea
            datos_mision = linea.strip().split(',')

            # Extraemos los valores desde el archivo
            nombre_mision = datos_mision[1]
            numero_planeta = datos_mision[2]
            numero_nave = datos_mision[3]
            armas = datos_mision[4].split('|')  # Lista de nombres de armas
            numero_integrantes = datos_mision[5].split('|')  # Lista de IDs de personajes

            # Buscar el objeto Planeta correspondiente al numero_planeta
            planeta_destino = next((planeta for planeta in planetas if planeta.id == numero_planeta), None)
            if not planeta_destino:
                print(f"Planeta con ID {numero_planeta} no encontrado.")
                continue

            # Buscar el objeto Nave correspondiente al numero_nave
            nave = next((nave for nave in naves if nave.id == numero_nave), None)
            if not nave:
                print(f"Nave con ID {numero_nave} no encontrada.")
                continue

            # Buscar los objetos Personaje correspondientes a los números de los integrantes
            integrantes = [personaje for personaje in personajes if personaje.id in numero_integrantes]
            if len(integrantes) != len(numero_integrantes):
                print(f"No se encontraron todos los personajes para la misión {nombre_mision}.")
                continue

            # Crear la misión y agregarla a la lista de misiones
            mision = Mision(nombre_mision, planeta_destino, nave, armas, integrantes)
            misiones.append(mision)

    return misiones

def crear_mision(planetas, naves, integrantes, usuario):
    """
    Permite al usuario crear una nueva misión, seleccionando los detalles desde listas predefinidas de planetas, naves y personajes.

    Args:
        planetas (list): Lista de objetos Planeta disponibles.
        naves (list): Lista de objetos Nave disponibles.
        integrantes (list): Lista de objetos Personaje disponibles.
        usuario (str): Nombre del usuario que está creando la misión.

    Returns:
        Mision: La misión creada, o None si no se puede crear una nueva misión.

    Proceso:
        - Se cargan las misiones existentes para verificar si el usuario ya ha alcanzado el límite de 5 misiones.
        - Se solicita al usuario que ingrese el nombre de la misión y seleccione el planeta, nave, armas e integrantes.
        - Se verifica que los integrantes seleccionados no se repitan.
        - La misión se crea y se guarda en el archivo de misiones del usuario.
    """
    misiones = cargar_misiones(usuario, planetas, naves, integrantes)
    if len(misiones) >= 5:
        print("Ya se han definido las 5 misiones permitidas.")
        return None
    
    nombre = input("Ingrese el nombre de la misión: ")
    
    # Selección del planeta destino
    print("Seleccione el planeta destino:")
    for i, planeta in enumerate(planetas):
        print(f"{i + 1}. {planeta.nombre}")
    planeta_index = int(input("Ingrese el número del planeta seleccionado: ")) - 1
    planeta_destino = planetas[planeta_index]
    
    # Selección de la nave
    print("Seleccione la nave a utilizar:")
    for i, nave in enumerate(naves):
        print(f"{i + 1}. {nave.nombre}")
    nave_index = int(input("Ingrese el número de la nave seleccionada: ")) - 1
    nave = naves[nave_index]

    # Entrada de armas
    armas_seleccionadas = []
    print("Escriba hasta 7 nombres de armas (escriba 'done' para terminar):")
    while len(armas_seleccionadas) < 7:
        arma = input(f"Arma {len(armas_seleccionadas)+1}: ")
        if arma.lower() == 'done':
            break
        armas_seleccionadas.append(arma)

    # Selección de integrantes
    integrantes_seleccionados = []
    print("Seleccione hasta 7 integrantes (escriba el número correspondiente; escriba '0' para terminar):")
    for i, integrante in enumerate(integrantes):
        print(f"{i + 1}. {integrante.nombre}")
    while len(integrantes_seleccionados) < 7:
        integrante_index = int(input("Ingrese el número del integrante seleccionado: ")) - 1
        if integrante_index == -1:
            break
        
        # Comprobación de duplicados
        seleccionado = integrantes[integrante_index]
        if seleccionado in integrantes_seleccionados:
            print(f"El integrante {seleccionado.nombre} ya ha sido seleccionado. Elija otro.")
            continue
        
        integrantes_seleccionados.append(seleccionado)
    
    # Crear la misión
    mision = Mision(nombre, planeta_destino, nave, armas_seleccionadas, integrantes_seleccionados)
    misiones.append(mision)
    guardar_misiones(misiones, usuario)
    return mision

def mostrar_misiones(misiones):
    """
    Muestra una lista de misiones almacenadas en la consola.

    Args:
        misiones (list): Lista de objetos Mision que se van a mostrar.

    Detalles mostrados:
        - Nombre de la misión
        - Planeta de destino
        - Nave utilizada
        - Lista de armas
        - Lista de integrantes
    """
    if not misiones:
        print("No hay misiones guardadas para mostrar.")
        return

    for idx, mision in enumerate(misiones, start=1):
        print(f"Misión {idx}:")
        print(f"  Nombre: {mision.nombre}")
        print(f"  Planeta Destino: {mision.planeta_destino.nombre}")
        print(f"  Nave: {mision.nave.nombre}")
        print(f"  Armas: {', '.join(mision.armas)}")
        print(f"  Integrantes: {', '.join([integrante.nombre for integrante in mision.integrantes])}")
        print()

def mostrar_misiones_usuario(usuario, planetas, naves, personajes):
    """
    Muestra las misiones asociadas a un usuario específico en la consola.

    Args:
        usuario (str): Nombre del usuario cuyas misiones se desean mostrar.
        planetas (list): Lista de objetos Planeta disponibles.
        naves (list): Lista de objetos Nave disponibles.
        personajes (list): Lista de objetos Personaje disponibles.

    Proceso:
        - Se cargan las misiones del usuario desde un archivo de texto.
        - Se muestra cada misión cargada en la consola, o se notifica si no hay misiones.
    """
    misiones = cargar_misiones(usuario, planetas, naves, personajes)
    
    if not misiones:
        print(f"No hay misiones guardadas para el usuario {usuario}.")
    else:
        print(f"Misiones guardadas para el usuario {usuario}:")
        mostrar_misiones(misiones)

def modificar_mision(usuario, planetas, naves, personajes):
    """
    Permite al usuario modificar los detalles de una misión existente.

    Args:
        usuario (str): Nombre del usuario que desea modificar la misión.
        planetas (list): Lista de objetos Planeta disponibles.
        naves (list): Lista de objetos Nave disponibles.
        personajes (list): Lista de objetos Personaje disponibles.

    Proceso:
        - Se cargan las misiones del usuario y se muestran para que el usuario seleccione cuál modificar.
        - Se permiten modificaciones en el nombre de la misión, el planeta destino, la nave, las armas y los integrantes.
        - Los cambios se guardan en el archivo de misiones del usuario.
    """
    misiones = cargar_misiones(usuario, planetas, naves, personajes)
    
    if not misiones:
        print(f"No hay misiones guardadas para el usuario {usuario}.")
        return
    
    # Mostrar las misiones y permitir al usuario seleccionar cuál modificar
    mostrar_misiones(misiones)
    
    try:
        num_mision = int(input("Ingrese el número de la misión que desea modificar: ")) - 1
        if num_mision < 0 or num_mision >= len(misiones):
            print("Número de misión no válido.")
            return
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return
    
    mision = misiones[num_mision]

    # Modificar nombre
    nuevo_nombre = input(f"Ingrese el nuevo nombre de la misión (actual: {mision.nombre}) o presione Enter para mantenerlo: ")
    if nuevo_nombre.strip():
        mision.nombre = nuevo_nombre.strip()

    # Modificar planeta destino
    print("Seleccione el nuevo planeta de destino:")
    for i, planeta in enumerate(planetas):
        print(f"{i + 1}. {planeta.nombre}")
    try:
        nuevo_planeta_index = input(f"Ingrese el número del nuevo planeta de destino (actual: {mision.planeta_destino.nombre}): ")
        if nuevo_planeta_index.strip():
            nuevo_planeta_index = int(nuevo_planeta_index) - 1
            if 0 <= nuevo_planeta_index < len(planetas):
                mision.planeta_destino = planetas[nuevo_planeta_index]
            else:
                print("Número de planeta no válido.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número válido para el planeta.")

    # Modificar nave
    print("Seleccione la nueva nave:")
    for i, nave in enumerate(naves):
        print(f"{i + 1}. {nave.nombre}")
    try:
        nueva_nave_index = input(f"Ingrese el número de la nueva nave (actual: {mision.nave.nombre}): ")
        if nueva_nave_index.strip():
            nueva_nave_index = int(nueva_nave_index) - 1
            if 0 <= nueva_nave_index < len(naves):
                mision.nave = naves[nueva_nave_index]
            else:
                print("Número de nave no válido.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número válido para la nave.")

    # Modificar armas
    armas_seleccionadas = []
    print("Escriba hasta 7 nombres de armas (escriba 'done' para terminar):")
    while len(armas_seleccionadas) < 7:
        arma = input(f"Arma {len(armas_seleccionadas)+1} (actual: {', '.join(mision.armas)}): ").strip()
        if arma.lower() == 'done':
            break
        elif arma:
            armas_seleccionadas.append(arma)
    if armas_seleccionadas:
        mision.armas = armas_seleccionadas

    # Modificar integrantes
    integrantes_seleccionados = []
    print("Seleccione hasta 7 integrantes (escriba el número correspondiente; escriba '0' para terminar):")
    for i, integrante in enumerate(personajes):
        print(f"{i + 1}. {integrante.nombre}")
    while len(integrantes_seleccionados) < 7:
        try:
            integrante_index = input(f"Seleccione el integrante {len(integrantes_seleccionados)+1} (actual: {', '.join([integrante.nombre for integrante in mision.integrantes])}): ")
            if integrante_index.strip():
                integrante_index = int(integrante_index) - 1
                if 0 <= integrante_index < len(personajes):
                    integrantes_seleccionados.append(personajes[integrante_index])
                else:
                    print("Número de integrante no válido.")
            elif integrante_index == '0':
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido para el integrante.")
    if integrantes_seleccionados:
        mision.integrantes = integrantes_seleccionados

    # Guardar las misiones actualizadas
    guardar_misiones(misiones, usuario)
    print("Misión modificada exitosamente.")
