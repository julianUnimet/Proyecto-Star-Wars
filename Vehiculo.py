from MedioTransporte import MedioTransporte

class Vehiculo(MedioTransporte):

    def __init__(self, id:str, nombre:str, longitud:str, capacidad:str, costo:str, pilotos:list) -> None:
        """Creacion del objeto vehiculo

        Args:
            id (str): id del vehiculo
            nombre (str): nombre del vehiculo
            longitud (str): longitud del vehiculo
            capacidad (str): capacidad del vehiculo
            costo (str): costo del vehiculo
            pilotos (list): lista de ids de los personajes que utilizan el vehiculo
            fabricante (str): fabricante del vehiculo
            clase_vehiculo (str): clase del vehiculo
        """
        super().__init__(id, nombre, longitud, capacidad, costo, pilotos)
        
    def informacion(self):
        super().informacion("vehiculo")