class Pelicula:
    #Agregar documentacion cuando ya se establescan todos los paramteros necesarios
    def __init__(self, titulo:str, episodio:int, fecha_lanzamiento:str, opening_crawl:str, director:str, especies:list, personajes:list, planetas:list) -> None:
        self.titulo = titulo
        self.episodio = episodio
        self.fecha_lanzamiento = fecha_lanzamiento
        self.opening_crawl = self.__tabulacion_opening(opening_crawl)
        self.director = director
        self.especies = especies
        self.personajes = personajes
        self.planetas = planetas

    def informacion(self):
        print(f"Titulo de la pelicula: {self.titulo}")
        print(f"Episodio: {self.episodio}")
        print(f"Dirigida por: {self.director}")
        print(f"Fecha de estreno: {self.fecha_lanzamiento}")
        print("Opening Crawl:")
        print()
        print(self.opening_crawl)
        print()

    def referenciar_personajes(self, personajes:list):
        #Este metodo se usara una vez se creen todas las listas de objetos y sirve para referenciar los objetos en funcion del id o se crean las peliculas
        #despues de crear los personajes, y especies y se les pasan las listas como argumentos
        pass

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
                

            
#Esto es para pruebas, luego se debe eliminar
#opening = "Luke Skywalker has returned to\r\nhis home planet of Tatooine in\r\nan attempt to rescue his\r\nfriend Han Solo from the\r\nclutches of the vile gangster\r\nJabba the Hutt.\r\n\r\nLittle does Luke know that the\r\nGALACTIC EMPIRE has secretly\r\nbegun construction on a new\r\narmored space station even\r\nmore powerful than the first\r\ndreaded Death Star.\r\n\r\nWhen completed, this ultimate\r\nweapon will spell certain doom\r\nfor the small band of rebels\r\nstruggling to restore freedom\r\nto the galaxy..."
#peli = Pelicula("A New Hope", 4, "1977-05-25", opening,"George Lucas", [], [], [])

#peli.informacion()
