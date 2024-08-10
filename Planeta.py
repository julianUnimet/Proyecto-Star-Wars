class Planeta:
    
    def __init__(self, id:str, nombre:str, periodo_orbita:str, periodo_rotacion:str, cantidad_habitantes:str, tipo_clima:str, peliculas:list) -> None:
        """Se crea el objeto planeta

        Args:
            id (str): id del planeta
            nombre (str): nombre del planeta
            periodo_orbita (str): periodo de orbita del planeta
            periodo_rotacion (str): periodo de rotacion del planeta
            cantidad_habitantes (str): cantidad de habitantes del planeta
            tipo_clima (str): tipo de clima del planeta
            peliculas (list): lista de todas las peliculas
            personajes (list): lista de todos los personajes
        """
        self.id = id
        self.nombre = nombre
        self.periodo_orbita = periodo_orbita
        self.periodo_rotacion = periodo_rotacion
        self.cantidad_habitantes = cantidad_habitantes
        self.tipo_clima = tipo_clima
        self.peliculas = self.referenciar_peliculas(peliculas)
        self.personajes = []

    def informacion(self):
        """Imprime en pantalla la informacion del planeta
        """
        print(f"ID: {self.id}")
        print(f"Nombre del planeta: {self.nombre}")
        print(f"Periodo de orbita: {self.periodo_orbita}")
        print(f"Periodo de rotacion: {self.periodo_rotacion}")
        print(f"Cantidad de habitantes: {self.cantidad_habitantes}")
        print(f"Tipo de clima: {self.tipo_clima}")
        print()
        print("Peliculas en las que aparece:")
        for pelicula in self.peliculas:
            print(f"\tEpisodio {pelicula.episodio}: {pelicula.titulo}")
        print()
        print("Personajes originarios de este planeta:")
        for personaje in self.personajes:
            print(f"\t{personaje.nombre}")
        print()

    def referenciar_peliculas(self, peliculas:list):
        """Este metodo compara el id del planeta con la lista de planetas de cada pelicula en peliculas y agrega la pelicula que contiene el indice del planeta

        Args:
            peliculas (list): lista de peliculas

        Returns:
            list: lista de objetos pelicula donde aparece el planeta
        """

        peliculas_aparece = []

        for pelicula in peliculas:
            if self.id in pelicula.planetas:
                peliculas_aparece.append(pelicula)

        return peliculas_aparece

    def referenciar_personajes(self, personajes:list):
        """Este metodo compara el id del planeta con el id del planeta de origen de cada personaje en personajes y agrega el personaje que contiene el indice del planeta. Llamar despues de crear los personajes

        Args:
            personajes (list): lista de objetos personajes
        Returns:
            list: lista de objetos personaje originarios de este planeta
        """

        personajes_de_este_planeta = []

        for personaje in personajes:
            if self.id == personaje.planeta_origen_id:
                personajes_de_este_planeta.append(personaje)

        self.personajes = personajes_de_este_planeta