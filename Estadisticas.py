import matplotlib.pyplot as plt
import pandas as pd


class Estadisticas:
    def __init__(self):
        self.planetas_datos = pd.read_csv('csv/planets.csv')
        self.naves_datos = pd.read_csv('csv/starships.csv')

    def personajes_por_planeta(self):
        personajes = self.planetas_datos["residents"] # se cargan los datos de residentes
        personajes = personajes.str.split(',').str.len() #Se cuentan los residentes

        self.__diagrama_barras("Cantidad de residentes por planeta", self.planetas_datos["name"], "Planetas", personajes, "Cantidad de residentes")

    def naves_por_longitud(self):
        longitud = self.naves_datos["length"]
        longitud = longitud.astype(float)
        nombre_naves = self.naves_datos["name"]

        self.__diagrama_barras("Comparacion de longitud de naves", nombre_naves, "Naves", longitud, "Longitud de naves", True)

    def naves_por_capacidad(self):
        capacidad = self.naves_datos["cargo_capacity"]
        capacidad = capacidad.astype(float)
        nombre_naves = self.naves_datos["name"]

        self.__diagrama_barras("Comparacion de capacidad de carga de naves", nombre_naves, "Naves", capacidad, "Capacidad de carga de naves", True)


    def naves_por_hiperimpulsor(self):
        hiperimpulsor = self.naves_datos["hyperdrive_rating"]
        hiperimpulsor = hiperimpulsor.astype(float)
        nombre_naves = self.naves_datos["name"]

        self.__diagrama_barras("Comparacion de hiperimpulsor de naves", nombre_naves, "Naves", hiperimpulsor, "Hiperimpulsor de naves")

    def naves_por_mglt(self):
        mglt = self.naves_datos["MGLT"]
        mglt = mglt.astype(float)
        nombre_naves = self.naves_datos["name"]

        self.__diagrama_barras("Comparacion de MGLT de naves", nombre_naves, "Naves", mglt, "MGLT de naves")

    def __diagrama_barras(self, titulo, datos_x, titulo_x, datos_y, titulo_y, escala_log=False):
        plt.bar(datos_x, datos_y)
        plt.title(titulo)
        plt.ylabel(titulo_y)
        if escala_log:
            plt.yscale("log")
        plt.xlabel(titulo_x)
        plt.xticks(rotation=90)
        plt.tight_layout() #Se ajusta la grafica para que no se corten los nombres
        plt.show()

    def tabla_estadisticos(self):
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
            "Promedio Velocidad Maxima en Atmosfera": [],
            "Moda Velocidad Maxima en Atmosfera": [],
            "Maximo Velocidad Maxima en Atmosfera": [],
            "Minimo Velocidad Maxima en Atmosfera": [],
            "Promedio Costo": [],
            "Moda Costo": [],
            "Maximo Costo": [],
            "Minimo Costo": []
        }

        # Calcular los estadisticos por clase de nave
        for clase in clases_naves:
            # Filtrar los datos por clase de nave
            datos_clase = self.naves_datos[self.naves_datos["starship_class"] == clase]
            

            # Calcular los estadisticos para el hiperimpulsor
            promedio_hiperimpulsor = datos_clase["hyperdrive_rating"].mean()
            moda_hiperimpulsor = datos_clase["hyperdrive_rating"].mode()[0]
            maximo_hiperimpulsor = datos_clase["hyperdrive_rating"].max()
            minimo_hiperimpulsor = datos_clase["hyperdrive_rating"].min()

            # Calcular los estadisticos para el MGLT
            promedio_mglt = datos_clase["MGLT"].mean()
            moda_mglt = datos_clase["MGLT"].mode()
            maximo_mglt = datos_clase["MGLT"].max()
            minimo_mglt = datos_clase["MGLT"].min()

            # Calcular los estadisticos para la velocidad maxima en atmosfera
            promedio_velocidad = datos_clase["max_atmosphering_speed"].mean()
            moda_velocidad = datos_clase["max_atmosphering_speed"].mode()
            maximo_velocidad = datos_clase["max_atmosphering_speed"].max()
            minimo_velocidad = datos_clase["max_atmosphering_speed"].min()

            # Calcular los estadisticos para el costo
            promedio_costo = datos_clase["cost_in_credits"].mean()
            moda_costo = datos_clase["cost_in_credits"].mode()
            maximo_costo = datos_clase["cost_in_credits"].max()
            minimo_costo = datos_clase["cost_in_credits"].min()

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
            estadisticos_por_clase["Promedio Velocidad Maxima en Atmosfera"].append(promedio_velocidad)
            estadisticos_por_clase["Moda Velocidad Maxima en Atmosfera"].append(moda_velocidad)
            estadisticos_por_clase["Maximo Velocidad Maxima en Atmosfera"].append(maximo_velocidad)
            estadisticos_por_clase["Minimo Velocidad Maxima en Atmosfera"].append(minimo_velocidad)
            estadisticos_por_clase["Promedio Costo"].append(promedio_costo)
            estadisticos_por_clase["Moda Costo"].append(moda_costo)
            estadisticos_por_clase["Maximo Costo"].append(maximo_costo)
            estadisticos_por_clase["Minimo Costo"].append(minimo_costo)

        # Crear un DataFrame a partir del diccionario de estadisticos
        estadisticos_naves = pd.DataFrame(estadisticos_por_clase)

        # Mostrar la tabla de estadisticos
        plt.figure(figsize=(12, 6))
        plt.axis('off')
        table = plt.table(cellText=estadisticos_naves.values, colLabels=estadisticos_naves.columns, loc='center', cellLoc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        
        # Ajustar el texto de los encabezados para que no se salgan de las celdas
        table.auto_set_column_width([0] + list(range(1, len(estadisticos_naves.columns))))
        table.scale(1, 1.5) # Increase the height of the table cells
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.auto_set_column_width([0] + list(range(1, len(estadisticos_naves.columns))))
        table.auto_set_column_width([0] + list(range(1, len(estadisticos_naves.columns))))
        plt.tight_layout() #Se ajusta la grafica para que no se corten los nombres
        plt.title("Estadisticos por Clase de Nave")
        plt.show()

        moda_hiperimpulsor = estadisticos_naves["Moda Hiperimpulsor"]
        moda_hiperimpulsor_values = estadisticos_naves["Moda Hiperimpulsor"].values

        #print(moda_hiperimpulsor)
        #print(moda_hiperimpulsor_values)

        print(estadisticos_naves["Promedio Velocidad Maxima en Atmosfera"])


#datos = Estadisticas()
#datos.tabla_estadisticos()
#datos.naves_por_mglt()

    