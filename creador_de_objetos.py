from Pelicula import Pelicula
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

crear_peliculas()