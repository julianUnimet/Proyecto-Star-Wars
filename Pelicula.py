class Pelicula:
    #Agregar documentacion cuando ya se estabelscan todos los paramteros necesarios
    def __init__(self, titulo:str, episodio:int, fecha_lanzamiento:str, opening_crawl:str, director:str) -> None:
        self.titulo = titulo
        self.episodio = episodio
        self.fecha_lanzamiento = fecha_lanzamiento
        self.opening_crawl = self.__tabulacion_opening(opening_crawl)
        self.director = director

    def informacion(self):
        print(f"Titulo de la pelicula: {self.titulo}")
        print(f"Episodio: {self.episodio}")
        print(f"Dirigida por: {self.director}")
        print(f"Fecha de estreno: {self.fecha_lanzamiento}")
        print("Openinh Crawl:")
        print()
        print(self.opening_crawl)
        print()

    def __tabulacion_opening(self, opening:str):
        """Es un metodo privado que agrega una tabulacion a cada linea del opening crawl para que cuando se imprima junto con la demas informacion se vea mas ordenado

        Args:
            opening (str): _description_

        Returns:
            _type_: _description_
        """
        opening = "\t" + opening

        for i in range(len(opening)):
            if opening[i] == '\n':
                partes_texto = [opening[:i+1], "\t", opening[i+1:]]
                opening = "".join(partes_texto)
                
        
        return opening
                

            
#Esto es para pruebas, luego se debe eliminar
opening = "It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon, the DEATH\r\nSTAR, an armored space\r\nstation with enough power\r\nto destroy an entire planet.\r\n\r\nPursued by the Empire's\r\nsinister agents, Princess\r\nLeia races home aboard her\r\nstarship, custodian of the\r\nstolen plans that can save her\r\npeople and restore\r\nfreedom to the galaxy...."
peli = Pelicula("A New Hope", 4, "1977-05-25", opening,"George Lucas")

peli.informacion()
