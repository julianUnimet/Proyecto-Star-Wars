

class Personaje:

    def __init__(self,id:str, nombre:str, id_planeta_origen:str, planetas:list, peliculas:list, genero, especies:list, naves:list, vehiculos:list) -> None:
        """Se crea el objeto personaje

        Args:
            id (str): id del personaje
            nombre (str): nombre del personaje
            id_planeta_origen (str): id del planeta de origen del personaje
            planetas (list): lista de todos los objetos planetas
            peliculas (list): lista de todos los objetos peliculas
            genero (_type_): genero del personaje
            especies (list): lista de todas las especies
            naves (list): lista de todos los objetos nave
            vehiculos (list): lista de todos los objetos vehiculo
        """         
        self.id = id
        self.nombre = nombre
        self.planeta_origen = self.referenciar_planeta(id_planeta_origen, planetas)
        self.peliculas = self.referenciar_peliculas(peliculas)
        self.genero = genero
        self.especie = self.referenciar_especie(especies)
        self.naves =  self.referenciar_medio_transporte(naves)
        self.vehiculos = self.referenciar_medio_transporte(vehiculos)
        
    def informacion(self):
        """Imprime en pantalla la informacion del personaje
        """
        print(f"ID: {self.id}")
        print(f"Nombre del personaje: {self.nombre}")
        print(f"Planeta de origen: {self.planeta_origen.nombre}")
        print(f"Genero: {self.genero}")
        print(f"Especie: {self.especie.nombre}")
        print()
        print(f"Peliculas en las que aparece:")
        for pelicula in self.peliculas:
            print(f"\tEpisodio {pelicula.episodio}: {pelicula.titulo}")
        print()
        print(f"Naves que pilota:")
        for nave in self.naves:
            print(f"\t{nave.nombre}")
        print()
        print(f"Vehiculos que pilota:")
        for vehiculo in self.vehiculos:
            print(f"\t{vehiculo.nombre}")
        print()
        
    def referenciar_planeta(self,id_planeta:str, planetas:list):
        """Referencia el objeto de tipo planeta en funcion del id

        Args:
            id_planeta (str): id del planeta
            planetas (list): lista de todos los objetos planetas

        Returns:
            list: lista con objeto planeta
        """
        for planeta in planetas:
            if id_planeta == planeta.id:
                return planeta
            
    def referenciar_peliculas(self, peliculas:list):
        """Este metodo compara el id del personaje con la lista de personajes de cada pelicula en peliculas y agrega la pelicula que contiene el indice del personaje
        """
        peliculas_aparece = []

        for pelicula in peliculas:
            if self.id in pelicula.personajes:
                peliculas_aparece.append(pelicula)
        
        return peliculas_aparece
    
    def referenciar_especie(self, especies:list):
        """Este metodo revisa si el personaje esta en la lista de personajes de cada especie y devuelve la especie a la que pertenece

        Args:
            especies (list): lista de especies

        Returns:
            Especie: objeto de tipo especie
        """
        for especie in especies:
            if self.id in especie.personajes_de_esta_especie:
                return especie

    def referenciar_medio_transporte(self, medio_transporte:list):
        """Este metodo referencia los objetos medios de transporte (nave, vehiculo) en funcion de los ids de los pilotos

        Args:
            medio_transporte (list): Lista de objetos medios de transporte (nave, vehiculo)

        Returns:
            list: Lista de objetos medios de transporte que pilota el personaje
        """
        medios_transporte_pilota = []

        for medio_transporte in medios_transporte_pilota:
            if self.id in medio_transporte.pilotos:
                medios_transporte_pilota.append(medio_transporte)
        
        return medios_transporte_pilota
    

