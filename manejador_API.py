#Aqui va todo lo relacionado a las peticiones al servidor
#Recomiendo que sean solo funciones, que no sea una clase en si
#Podriamos hace aqui de una vez la creacion de los objetos para cada planeta, personaje, etc. Sin embargo con eso le estarimos dando dos responsabilidades a una misma libreria
import requests

def obtener_informacion(link:str):
    """Optiene la informacion desde el enlace link

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

