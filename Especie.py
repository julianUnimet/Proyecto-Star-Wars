
class Especie:

    def __init__(self,id:str, nombre:str, altura:str, clasificacion:str, lengua_materna:str, planeta_origen, pesonajes_de_esta_especie:list, Peliculas:list) -> None:
        self.id = id
        self.nombre = nombre 
        self.altura = altura
        self.clasificacion = clasificacion
        self.lengua_materna = lengua_materna
        self.planeta_origen = planeta_origen
        self.personajes_de_esta_especie = pesonajes_de_esta_especie
        self.peliculas = Peliculas #Para esto tengo que buscar dentro de peliculas cuales son las peliculas en las que aparece esta especie

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
        elif self.planeta_origen != None: #Se valida si la especie no tiene planeta de origen
            print(f"Planeta de origen: {self.planeta_origen.nombre}")
        else:
            print("Planeta de origen: Desconocido")

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
            print(f"\t{pelicula.titulo}")
        print()
        
