import matplotlib.pyplot as plt
import pandas as pd


class Estadisticas:
    def __init__(self):
        self.planetas_datos = pd.read_csv('csv/planets.csv')
        self.naves_datos = pd.read_csv('csv/starships.csv')

    def personajes_por_planeta(self):
        """Crea un diagrama de barras con la cantidad de personajes por plan
        """
        personajes = self.planetas_datos["residents"] # se cargan los datos de residentes
        personajes = personajes.str.split(',').str.len() #Se cuentan los residentes
        self.__diagrama_barras("Cantidad de residentes por planeta", self.planetas_datos["name"], "Planetas", personajes, "Cantidad de residentes")

    def naves_por_longitud(self):
        """Crea un diagrama de barras con la longitud de las naves
        """
        nombre_naves, longitud = self.__valores_para_diagrama_barras("length")
        self.__diagrama_barras("Comparacion de longitud de naves", nombre_naves, "Naves", longitud, "Longitud de naves", True)

    def naves_por_capacidad(self):
        """Crea un diagrama de barras con la capacidad de las naves
        """
        nombre_naves, capacidad = self.__valores_para_diagrama_barras("cargo_capacity")
        self.__diagrama_barras("Comparacion de capacidad de carga de naves", nombre_naves, "Naves", capacidad, "Capacidad de carga de naves", True)

    def naves_por_hiperimpulsor(self):
        """Crea un diagrama de barras con el hiperimpulsor de las naves
        """
        nombre_naves, hiperimpulsor = self.__valores_para_diagrama_barras("hyperdrive_rating")
        self.__diagrama_barras("Comparacion de hiperimpulsor de naves", nombre_naves, "Naves", hiperimpulsor, "Hiperimpulsor de naves")

    def naves_por_mglt(self):
        """Crea un diagrama de barras con el mglt de las naves
        """
        nombre_naves, mglt = self.__valores_para_diagrama_barras("MGLT")
        self.__diagrama_barras("Comparacion de MGLT de naves", nombre_naves, "Naves", mglt, "MGLT de naves")

    def __valores_para_diagrama_barras(self, propiedad:str):
        """Extrae los valores de una propiedad de las naves para crear un diagrama de barras.

        Args:
            propiedad (str): nombre de la propiedad a extraer, valores posibles: "length", "cargo_capacity", "hyperdrive_rating", "MGLT"

        Returns:
            _type_: nombres_naves, valores_propiedad
        """
        
        nombres_naves = self.naves_datos["name"]
        valores_propiedad = self.naves_datos[propiedad]
        valores_propiedad = valores_propiedad.astype(float)

        return nombres_naves, valores_propiedad

    def __diagrama_barras(self, titulo:str, datos_x, titulo_x:str, datos_y, titulo_y:str, escala_log=False):
        """Crea un diagrama de barras

        Args:
            titulo (str): Titulo de la grafica
            datos_x (_type_): Valores del eje x
            titulo_x (str): Titulo del eje x
            datos_y (_type_): Valores del eje y
            titulo_y (str): Titulo del eje y
            escala_log (bool, optional): True para colocar el eje y en escala logaritmica. Defaults to False.
        """        
        plt.bar(datos_x, datos_y)
        plt.title(titulo)
        plt.ylabel(titulo_y)
        if escala_log:
            plt.yscale("log")
        plt.xlabel(titulo_x)
        plt.xticks(rotation=90)
        plt.tight_layout() #Se ajusta la grafica para que no se corten los nombres
        plt.show()

    def __tabla_estadisticos(self):
        """Calcula los estadisticos de las propiedades de las naves por clase de nave.

        Returns:
            DataFrame: tabla con los estadisticos de las propiedades de las naves por clase de nave
        """
        # Obtener las clases de nave únicas
        clases_naves = sorted(self.naves_datos["starship_class"].unique())

        # Crear un diccionario para almacenar los estadisticos por clase de nave
        estadisticos_por_clase = {
            "Clase de Nave": [],
            "Promedio Hiperimpulsor": [],
            "Moda Hiperimpulsor": [],
            "Maximo Hiperimpulsor": [],
            "Minimo Hiperimpulsor": [],
            "Promedio MGLT": [],
            "Moda MGLT": [],
            "Maximo MGLT": [],
            "Minimo MGLT": [],
            "Promedio Vel. Max. en Atmos.": [],
            "Moda Vel. Max. en Atmos.": [],
            "Maximo Vel. Max. en Atmos.": [],
            "Minimo Vel. Max. en Atmos.": [],
            "Promedio Costo": [],
            "Moda Costo": [],
            "Maximo Costo": [],
            "Minimo Costo": []
        }

        # Calcular los estadisticos por clase de nave
        for clase in clases_naves:
            # Filtrar los datos por clase de nave
            datos_clase = self.naves_datos[self.naves_datos["starship_class"] == clase]
           
            # Calcular los estadisticos para la as propiedades
            promedio_velocidad, moda_velocidad, maximo_velocidad, minimo_velocidad = self.valores_estadisticos(datos_clase, "max_atmosphering_speed")
            promedio_costo, moda_costo, maximo_costo, minimo_costo = self.valores_estadisticos(datos_clase, "cost_in_credits")
            promedio_mglt, moda_mglt, maximo_mglt, minimo_mglt = self.valores_estadisticos(datos_clase, "MGLT")
            promedio_hiperimpulsor, moda_hiperimpulsor, maximo_hiperimpulsor, minimo_hiperimpulsor = self.valores_estadisticos(datos_clase, "hyperdrive_rating")

            # Agregar los estadisticos al diccionario
            estadisticos_por_clase["Clase de Nave"].append(clase)
            estadisticos_por_clase["Promedio Hiperimpulsor"].append(promedio_hiperimpulsor)
            estadisticos_por_clase["Moda Hiperimpulsor"].append(moda_hiperimpulsor)
            estadisticos_por_clase["Maximo Hiperimpulsor"].append(maximo_hiperimpulsor)
            estadisticos_por_clase["Minimo Hiperimpulsor"].append(minimo_hiperimpulsor)
            estadisticos_por_clase["Promedio MGLT"].append(promedio_mglt)
            estadisticos_por_clase["Moda MGLT"].append(moda_mglt)
            estadisticos_por_clase["Maximo MGLT"].append(maximo_mglt)
            estadisticos_por_clase["Minimo MGLT"].append(minimo_mglt)
            estadisticos_por_clase["Promedio Vel. Max. en Atmos."].append(promedio_velocidad)
            estadisticos_por_clase["Moda Vel. Max. en Atmos."].append(moda_velocidad)
            estadisticos_por_clase["Maximo Vel. Max. en Atmos."].append(maximo_velocidad)
            estadisticos_por_clase["Minimo Vel. Max. en Atmos."].append(minimo_velocidad)
            estadisticos_por_clase["Promedio Costo"].append(promedio_costo)
            estadisticos_por_clase["Moda Costo"].append(moda_costo)
            estadisticos_por_clase["Maximo Costo"].append(maximo_costo)
            estadisticos_por_clase["Minimo Costo"].append(minimo_costo)
        
        estadisticos_naves = pd.DataFrame(estadisticos_por_clase) # Crear un DataFrame a partir del diccionario de estadisticos


        return estadisticos_naves

    def valores_estadisticos(self, datos_clase, propiedad:str):
        """Calcula los valores estadisticos de una propiedad de una clase de nave.

        Args:
            datos_clase (_type_): Datos de la clase de nave
            propiedad (str): Propiedad de la nave, valores posible: "max_atmosphering_speed", "cost_in_credits", "MGLT", "hyperdrive_rating"
        Returns:
            _type_: promedio, moda, maximo, minimo
        """
        promedio_velocidad = round(datos_clase[propiedad].mean(), 2)
        moda_velocidad = datos_clase[propiedad].mode().values
        maximo_velocidad = datos_clase[propiedad].max()
        minimo_velocidad = datos_clase[propiedad].min()
        return promedio_velocidad,moda_velocidad,maximo_velocidad,minimo_velocidad
    
    def mostrar_estadisticos_propiedad(self, propiedad:str):
        """Imprime en pantalla una tabla con los estadisticos de la propiedad seleccionada.

        Args:
            propiedad (str): Valores posibles: "Hiperimpulsor", "MGLT", "Velocidad Maxima en Atmosfera", "Costo"
        """        
        estadisticos_naves = self.__tabla_estadisticos()
        
        columnas_propiedad = ["Clase de Nave", f"Promedio {propiedad}", f"Moda {propiedad}", f"Maximo {propiedad}", f"Minimo {propiedad}"] # Obtener las columnas correspondientes a la propiedad seleccionada
        
        estadisticos_propiedad = estadisticos_naves[columnas_propiedad] # Filtrar las columnas del DataFrame de estadisticos

        print(estadisticos_propiedad)
        print()
        input("Ingrese cualquier tecla para continuar: ")


    