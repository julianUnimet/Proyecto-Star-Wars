#Aqui va todo lo relacionado a las peticiones al servidor
#Recomiendo que sean solo funciones, que no sea una clase en si
#Podriamos hace aqui de una vez la creacion de los objetos para cada planeta, personaje, etc. Sin embargo con eso le estarimos dando dos responsabilidades a una misma libreria
import requests
import funciones

def obtener_informacion(link:str):
    """Obtiene la informacion desde el enlace link

    Args:
        link (str): URL de la informacion

    Returns:
        _type_: Informacion optenida en formato json
    """
    informacion = requests.get(link)

    if informacion.status_code == 200:
        informacion = informacion.json()
        return informacion        
    else:
        print(f"Error: {informacion.status_code}")

def obtener_informacion_listas_diccionario_con_url(url:str):
    """Obtiene informacion del url y de las url que estan en la lista de diccionarios que se obtiene de la informacion del url

    Args:
        url (str): URL de la informacion

    Returns:
        list: Lista de diccionarios con la informacion de cada objeto
    """

    informacion = []

    info_preliminar = obtener_informacion(url) #Obtenemos la informacion preliminar de la url 
    info_preliminar = info_preliminar["results"] #Extraemos la lista de diccionarios que tiene la informacion de cada objeto

    for diccionario in info_preliminar:
        info = obtener_informacion(diccionario["url"])#Extraemos la informacion de cada objeto
        informacion.append(info) #Agregamos la informacion a la lista

    return informacion
    
def obtener_informacion_de_varias_paginas(url:str):
    """Obtiene la informacion de varias paginas

    Args:
        url (str): URL de la informacion

    Returns:
        list: Lista de diccionarios con la informacion de cada objeto
    """

    informacion = []
    next_url = obtener_informacion(url)["next"]

    while url != None:
        info_preliminar = obtener_informacion_listas_diccionario_con_url(url)
        informacion += info_preliminar
        url = next_url
        if url != None:        
            next_url = obtener_informacion(url)["next"]
        print("Cargando...")

    funciones.limpiar_consola()

    return informacion


            




