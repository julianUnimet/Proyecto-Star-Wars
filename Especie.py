
class Especie:

    def __init__(self,id:str, nombre:str, altura:str, clasificacion:str, lengua_materna:str, planeta_origen:str, planetas:list, pesonajes_de_esta_especie:list, peliculas:list) -> None:
        """Creacion del objeto especie

        Args:
            id (str): id de la especie
            nombre (str): nombre de la especie
            altura (str): altura promedio de la especie
            clasificacion (str): clasificacion de la especie
            lengua_materna (str): lengua materna de la especie
            planeta_origen (str): id del planeta de origen de la especie
            planetas (list): lista de todos los planeta
            pesonajes_de_esta_especie (list): lista de ids de los personajes
            peliculas (list): lista de todas las peliculas
        """

        self.id = id
        self.nombre = nombre 
        self.altura = altura
        self.clasificacion = clasificacion
        self.lengua_materna = lengua_materna
        self.planeta_origen = self.referenciar_planeta(planeta_origen, planetas)
        self.personajes_de_esta_especie = pesonajes_de_esta_especie
        self.peliculas = self.referenciar_peliculas(peliculas) #Para esto tengo que buscar dentro de peliculas cuales son las peliculas en las que aparece esta especie

    def informacion(self):
        """Imprime en pantalla la informacion de la especie
        """
        print(f"ID: {self.id}")
        print(f"Nombre de la especie: {self.nombre}")
        print(f"Altura promedio: {self.altura}")
        print(f"Clasificacion: {self.clasificacion}")
        print(f"Lengua materna: {self.lengua_materna}")

        if type(self.planeta_origen) == str: #Se ejecuta si por alguna razon aun no se ha referenciado el objeto planeta
            print(f"Planeta de origen: {self.planeta_origen}")
        else:
            print(f"Planeta de origen: {self.planeta_origen.nombre}")

        print()
        print("Personajes de esta especie:")
        for personaje in self.personajes_de_esta_especie:
            if type(personaje) == str: # se ejecuta si por alguna razon aun no se ha referenciado el objeto personaje y solo estan los ids
                print(f"\t{personaje}")
            else:
                print(f"\t{personaje.nombre}")
        print()
        print("Peliculas en las que aparece:")
        for pelicula in self.peliculas:
            print(f"\tEpisodio {pelicula.episodio}: {pelicula.titulo}")
        print()
        

    def referenciar_peliculas(self, peliculas:list):
        """Este metodo compara el id de la especie con la lista de especie de cada pelicula en peliculas y agrega la pelicula que contiene el indice de la especie

        Args:
            peliculas (list): lista de peliculas

        Returns:
            list: lista de objetos pelicula donde aparece la especie
        """

        peliculas_aparece = []

        for pelicula in peliculas:
            if self.id in pelicula.especies:
                peliculas_aparece.append(pelicula)

        return peliculas_aparece
    
    def referenciar_planeta(self, planeta_id:str, planetas:list):
        
        for planeta in planetas:
            if planeta_id == planeta.id:
                return planeta

    def referenciar_personajes(self, personajes:list):
        """Este metodo compara las ids de los personajes de esta especie con el id de cada personaje en personajes y agrega el personaje que contiene el indice del planeta. Llamar despues de crear los personajes

        Args:
            personajes (list): lista de objetos personajes
        Returns:
            list: lista de objetos personaje originarios de este planeta
        """

        personajes_de_esta_especie = []

        for personaje in personajes:
            if personaje.id in self.personajes_de_esta_especie:
                personajes_de_esta_especie.append(personaje)

        self.personajes_de_esta_especie = personajes_de_esta_especie