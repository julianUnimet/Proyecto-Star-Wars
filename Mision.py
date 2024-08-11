import Planeta
import Nave
import Personaje
import json
import os

class Mision:
    def __init__(self, nombre, planeta_destino, nave, armas, integrantes):
        self.nombre = nombre
        self.planeta_destino = planeta_destino
        self.nave = nave
        self.armas = armas  # Ahora es una lista de nombres (strings)
        self.integrantes = integrantes

    def __str__(self):
        return (f'Misión: {self.nombre}\n'
                f'Planeta Destino: {self.planeta_destino.nombre}\n'
                f'Nave: {self.nave.nombre}\n'
                f'Armas: {", ".join(self.armas)}\n'  # Ya no es necesario acceder a nombre de objetos
                f'Integrantes: {", ".join([integrante.nombre for integrante in self.integrantes])}\n')

def guardar_misiones(misiones, usuario):
    archivo_misiones = f'misiones_{usuario}.txt'  # El archivo se asocia con el usuario
    with open(archivo_misiones, 'w') as file:
        for mision in misiones:
            mision_data = {
                'nombre_mision': mision.nombre,
                'numero_planeta': mision.planeta_destino.id,  # Asumimos que el ID es un número o identificador único
                'numero_nave': mision.nave.id,  # Asumimos que el ID es un número o identificador único
                'armas': mision.armas,  # Ya es una lista de nombres de armas
                'numero_integrantes': [integrante.id for integrante in mision.integrantes]  # Asumimos que el ID es un número
            }
            # Escribir los datos de la misión en el archivo, incluyendo el nombre de usuario
            file.write(f"{usuario},{mision_data['nombre_mision']},{mision_data['numero_planeta']},{mision_data['numero_nave']},{'|'.join(mision_data['armas'])},{'|'.join(map(str, mision_data['numero_integrantes']))}\n")


def cargar_misiones(usuario, planetas, naves, personajes):
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
            armas = datos_mision[4].split('|')  # Armas ya es una lista de strings
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

            # Buscar los objetos Personaje correspondientes a los numeros de los integrantes
            integrantes = [personaje for personaje in personajes if personaje.id in numero_integrantes]
            if len(integrantes) != len(numero_integrantes):
                print(f"No se encontraron todos los personajes para la misión {nombre_mision}.")
                continue

            # Crear la misión y agregarla al array de misiones
            mision = Mision(nombre_mision, planeta_destino, nave, armas, integrantes)
            misiones.append(mision)

    return misiones




def crear_mision(planetas, naves, integrantes, usuario):
    misiones = cargar_misiones(usuario,planetas,naves,integrantes)
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
        integrantes_seleccionados.append(integrantes[integrante_index])
    
    # Crear la misión
    mision = Mision(nombre, planeta_destino, nave, armas_seleccionadas, integrantes_seleccionados)
    misiones.append(mision)
    guardar_misiones(misiones, usuario)
    return mision

def mostrar_misiones(misiones):
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
    # Cargar las misiones del usuario
    misiones = cargar_misiones(usuario, planetas, naves, personajes)
    
    # Mostrar las misiones cargadas
    if not misiones:
        print(f"No hay misiones guardadas para el usuario {usuario}.")
    else:
        print(f"Misiones guardadas para el usuario {usuario}:")
        mostrar_misiones(misiones)

def modificar_mision(usuario, planetas, naves, personajes):
    # Cargar las misiones del usuario
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
