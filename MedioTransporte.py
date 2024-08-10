class MedioTransporte:
    
    def __init__(self, id:str, nombre:str, longitud:str, capacidad:str, costo:str, pilotos:list) -> None:
        """Creacion del objeto nave

        Args:
            id (str): id
            nombre (str): nombre
            longitud (str): longitud
            capacidad_carga (str): capacidad de carga
            costo (str): costo de la nave
            pilotos (list): lista de ids de los personajes que utilizan el medio de transporte
        """
        self.id = id
        self.nombre = nombre
        self. longitud = longitud
        self.capacidad = capacidad
        self.costo = costo
        self.pilotos = pilotos
        
    def informacion(self, tipo:str):
        """Imprime en pantalla la informacion
        """
        print(f"ID: {self.id}")
        print(f"Nombre de {tipo}: {self.nombre}")
        print(f"Longitud de {tipo}: {self.longitud}")
        print(f"Capacidad de carga: {self.capacidad}")
        print(f"Costo de {tipo}: {self.costo}")