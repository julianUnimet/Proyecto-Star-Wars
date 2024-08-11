from MedioTransporte import MedioTransporte
class Nave(MedioTransporte):

    def __init__(self, id:str, nombre:str, longitud_nave:str, capacidad_carga:str, costo:str, pilotos:list, clasificacion_hiperimpulsor:str, mglt:str,) -> None:
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
        super().__init__(id, nombre, longitud_nave, capacidad_carga, costo, pilotos)
        self.clasificacion_hiperimpulsor = clasificacion_hiperimpulsor
        self.mglt = mglt
        

    def informacion(self):
        """Imprime en pantalla la informacion de la nave
        """
        super().informacion("nave")
        print(f"Clasificacion del hiperimpulsor: {self.clasificacion_hiperimpulsor}")
        print(f"MGLT: {self.mglt}")
        print()
        print("Pilotos de la nave:")
        for piloto in self.pilotos:
            print(f"\t{piloto}")
        print()
        
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'longitud_nave': self.longitud_nave,
            'capacidad_carga': self.capacidad_carga,
            'costo': self.costo,
            'pilotos': self.pilotos,  # Suponiendo que son IDs o nombres, si son objetos necesitas convertirlos también
            'clasificacion_hiperimpulsor': self.clasificacion_hiperimpulsor,
            'mglt': self.mglt
        }
