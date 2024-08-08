from Pelicula import Pelicula
from Especie import Especie
from Planeta import Planeta
import manejador_API

def crear_peliculas():
    """Crea los objetos de tipo Pelicula

    Returns:
        list: retorna una lista con los objetos de tipo pelicula
    """

    peliculasOBJ = [] #Lista de objetos

    info_peliculas = manejador_API.obtener_informacion("https://www.swapi.tech/api/films")

    for info_pelicula in info_peliculas["result"]:
        titulo = info_pelicula["properties"]["title"]
        episodio = info_pelicula["properties"]["episode_id"]
        fecha_lanzamiento = info_pelicula["properties"]["release_date"]
        opening_crawl = info_pelicula["properties"]["opening_crawl"]
        director = info_pelicula["properties"]["director"]
        especies = extractor_id_desde_url(info_pelicula["properties"]["species"])    
        personajes = extractor_id_desde_url(info_pelicula["properties"]["characters"])  
        planetas = extractor_id_desde_url(info_pelicula["properties"]["planets"]) 

        peliculasOBJ.append(Pelicula(titulo, episodio, fecha_lanzamiento, opening_crawl, director, especies, personajes, planetas))

    return peliculasOBJ 

def crear_especies(peliculas:list, planetas:list):
    """Crea los objetos de tipo Especie
    
    Args:
        peliculas (list): Lista de objetos de tipo pelicula
        planetas (list): Lista de objetos de tipo planeta

    Returns:
        list[Especie]: retorna una lista con los objetos de tipo especie
    """
    especiesOBJ = [] #Lista de objetos

    info_especies = manejador_API.obtener_informacion_de_varias_paginas("https://www.swapi.tech/api/species")

    for info_especie in info_especies:

        id = info_especie["result"]["uid"]

        propiedades = info_especie["result"]["properties"]
        nombre = propiedades["name"]
        altura = propiedades["average_height"]
        clasificacion = propiedades["classification"]
        lengua_materna = propiedades["language"]
        planeta_origen = extractor_id_desde_url([propiedades["homeworld"]])[0] #Solo se espera un id, por lo que paso el id y no una lista
        personajes_de_esta_especie = extractor_id_desde_url(propiedades["people"])        

        especiesOBJ.append(Especie(id, nombre, altura, clasificacion, lengua_materna, planeta_origen, planetas, personajes_de_esta_especie, peliculas))

    return especiesOBJ

def crear_planetas(peliculas:list, personajes:list):
    """Crea los objetos tipo Planeta

    Args:
        peliculas (list): Lista de objetos de tipo pelicula
        personajes (list): Lista de objetos de tipo personaje

    Returns:
        list[Planetas]: Lista de objetos de tipo Planeta
    """

    planetasOBJ = [] #Lista de objetos

    info_planetas = manejador_API.obtener_informacion_de_varias_paginas("https://www.swapi.tech/api/planets")

    for info_planeta in info_planetas:
        id = info_planeta["result"]["uid"]    

        propiedades = info_planeta["result"]["properties"]
        nombre = propiedades["name"]
        perdiodo_orbita = propiedades["orbital_period"]
        periodo_rotacion = propiedades["rotation_period"]
        cantidad_habitantes = propiedades["population"]
        tipo_clima = propiedades["climate"]

        planetasOBJ.append(Planeta(id, nombre, perdiodo_orbita, periodo_rotacion, cantidad_habitantes, tipo_clima, peliculas, personajes))

    return planetasOBJ







def extractor_id_desde_url(lista_urls:list):
    """Esta funcion extrae el id de los url aprovechando que el id esta al final del url. Solo funciona si los unicos valores numericos que aparecen son los del id

    Args:
        lista_urls (list): Lista de url

    Returns:
        list: lista de ids
    """
    ids = []
    for url in lista_urls:
        id = ""
        for i in url:
            if i.isdigit():
                id += i

        if id != "":
            ids.append(id)

    return ids
