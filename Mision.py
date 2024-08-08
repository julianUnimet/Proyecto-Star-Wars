import Planeta
import Nave
import Arma
import Personaje
import json
import os

class Mision:
    def __init__(self, nombre, planeta_destino, nave, armas, integrantes):
        self.nombre = nombre
        self.planeta_destino = planeta_destino
        self.nave = nave
        self.armas = armas
        self.integrantes = integrantes

    def __str__(self):
        return (f'Misión: {self.nombre}\n'
                f'Planeta Destino: {self.planeta_destino.nombre}\n'
                f'Nave: {self.nave.nombre}\n'
                f'Armas: {", ".join([arma.nombre for arma in self.armas])}\n'
                f'Integrantes: {", ".join([integrante.nombre for integrante in self.integrantes])}\n')

def guardar_misiones(misiones, usuario):
    archivo_misiones = f'misiones_{usuario}.txt'
    with open(archivo_misiones, 'w') as file:
        json.dump([mision.__dict__ for mision in misiones], file, indent=4, default=lambda o: o.__dict__)

def cargar_misiones(usuario):
    archivo_misiones = f'misiones_{usuario}.txt'
    if not os.path.exists(archivo_misiones):
        return []
    with open(archivo_misiones, 'r') as file:
        misiones_data = json.load(file)
    misiones = []
    for mision_data in misiones_data:
        planeta = Planeta(mision_data['planeta_destino']['id'], mision_data['planeta_destino']['nombre'],
                          mision_data['planeta_destino']['periodo_orbita'], mision_data['planeta_destino']['periodo_rotacion'],
                          mision_data['planeta_destino']['cantidad_habitantes'], mision_data['planeta_destino']['tipo_clima'],
                          mision_data['planeta_destino']['peliculas'], mision_data['planeta_destino']['personajes'])
        nave = Nave(mision_data['nave']['id'], mision_data['nave']['nombre'], mision_data['nave']['longitud'],
                    mision_data['nave']['capacidad_carga'], mision_data['nave']['clasificacion_hiperimpulsor'], mision_data['nave']['MGLT'])
        armas = [Arma(arma['id'], arma['nombre'], arma['tipo']) for arma in mision_data['armas']]
        integrantes = [Personaje(integrante['id'], integrante['nombre'], integrante['especie'], integrante['genero']) for integrante in mision_data['integrantes']]
        misiones.append(Mision(mision_data['nombre'], planeta, nave, armas, integrantes))
    return misiones

def crear_mision(planetas, naves, armas, integrantes, usuario):
    misiones = cargar_misiones(usuario)
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
    
    # Selección de armas
    armas_seleccionadas = []
    print("Seleccione hasta 7 armas (escriba el número correspondiente; escriba '0' para terminar):")
    for i, arma in enumerate(armas):
        print(f"{i + 1}. {arma.nombre}")
    while len(armas_seleccionadas) < 7:
        arma_index = int(input("Ingrese el número del arma seleccionada: ")) - 1
        if arma_index == -1:
            break
        armas_seleccionadas.append(armas[arma_index])
    
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
