class Pelicula:
    
    def __init__(self, titulo:str, episodio:int, fecha_lanzamiento:str, opening_crawl:str, director:str, especies:list, personajes:list, planetas:list) -> None:
        """Creacion del objeto pelicula

        Args:
            titulo (str): titulo de la pelicula
            episodio (int): episodio de la pelicula
            fecha_lanzamiento (str): fecha de lanzamiento de la pelicula
            opening_crawl (str): opening crawl de la pelicula
            director (str): director de la pelicula
            especies (list): lista de ids de las especies que aparecen en la pelicula
            personajes (list): lista de ids de los personajes que aparecen en la pelicula
            planetas (list): lista de ids de los planetas que aparecen en la pelicula
        """
        self.titulo = titulo
        self.episodio = episodio
        self.fecha_lanzamiento = fecha_lanzamiento
        self.opening_crawl = self.__tabulacion_opening(opening_crawl)
        self.director = director
        self.especies = especies
        self.personajes = personajes
        self.planetas = planetas

    def informacion(self):
        """Imprime en pantalla la informacion de la pelicula
        """
        print(f"Titulo de la pelicula: {self.titulo}")
        print(f"Episodio: {self.episodio}")
        print(f"Dirigida por: {self.director}")
        print(f"Fecha de estreno: {self.fecha_lanzamiento}")
        print("Opening Crawl:")
        print()
        print(self.opening_crawl)
        print()


    def __tabulacion_opening(self, opening:str):
        """Es un metodo privado que agrega una tabulacion a cada linea del opening crawl para que cuando se imprima junto con la demas informacion se vea mas ordenado

        Args:
            opening (str): El opening Crawl

        Returns:
            str: Retorna el opening pero con una tabulacion al inicio de cada linea
        """
        opening = "\t" + opening
        i = 0
        while i <= len(opening)-1:
            if opening[i] == '\n':
                partes_texto = [opening[:i+1], "\t", opening[i+1:]]
                opening = "".join(partes_texto)

            i+= 1
        
        return opening
                
    def to_dict(self):
        """Convierte el objeto Pelicula en un diccionario para facilitar la serialización.

        Returns:
            dict: Un diccionario con los datos de la película.
        """
        return {
            'titulo': self.titulo,
            'episodio': self.episodio,
            'fecha_lanzamiento': self.fecha_lanzamiento,
            'opening_crawl': self.opening_crawl,
            'director': self.director,
            'especies': self.especies,  # Suponiendo que es una lista de IDs o strings
            'personajes': self.personajes,  # Suponiendo que es una lista de IDs o strings
            'planetas': self.planetas  # Suponiendo que es una lista de IDs o strings
        }
