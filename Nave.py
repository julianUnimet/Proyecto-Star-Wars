
class Nave():

    def __init__(self, id:str, nombre:str, longitud_nave:str, capacidad_carga:str, clasificacion_hiperimpulsor:str, mglt:str, costo:str, pilotos:list) -> None:
        """Creacion del objeto nave

        Args:
            id (str): id de la nave
            nombre (str): nombre de la nave
            longitud_nave (str): longitud de la nave   
            capacidad_carga (str): capacidad de carga de la nave
            clasificacion_hiperimpulsor (str): clasificacion del hiperimpulsor de la nave
            mglt (str): mglt de la nave
            costo (str): costo de la nave
            pilotos (list): lista de ids de los personajes que utilizan la nave
        """
        self.id = id
        self.nombre = nombre
        self.longitud_nave = longitud_nave
        self.capacidad_carga = capacidad_carga
        self.clasificacion_hiperimpulsor = clasificacion_hiperimpulsor
        self.mglt = mglt
        self.costo = costo
        self.pilotos = pilotos

    def informacion(self):
        """Imprime en pantalla la informacion de la nave
        """
        print(f"ID: {self.id}")
        print(f"Nombre de la nave: {self.nombre}")
        print(f"Longitud de la nave: {self.longitud_nave}")
        print(f"Capacidad de carga: {self.capacidad_carga}")
        print(f"Clasificacion del hiperimpulsor: {self.clasificacion_hiperimpulsor}")
        print(f"MGLT: {self.mglt}")
        print(f"Costo de la nave: {self.costo}")
        print()
        print("Pilotos de la nave:")
        for piloto in self.pilotos:
            print(f"\t{piloto}")
        print()
