import csv
import os
import Arma  # Asegúrate de que la clase Arma esté en un archivo llamado arma.py o ajusta la importación según sea necesario

def leer_armas_desde_csv():
    """
    Lee el archivo CSV 'weapons.csv' ubicado en la carpeta 'csv' y convierte cada fila en un objeto Arma.

    Returns:
        list[Arma]: Lista de objetos Arma creados a partir de los datos en el archivo CSV.
    """
    armas = []
    ruta_csv = os.path.join('csv', 'weapons.csv')

    with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
        lector_csv = csv.DictReader(csvfile)
        for fila in lector_csv:
            arma = Arma(
                id=fila['id'],
                nombre=fila['name'],
                modelo=fila['model'],
                fabricante=fila['manufacturer'],
                costo_en_creditos=fila['cost_in_credits'],
                longitud=fila['length'],
                tipo=fila['type'],
                descripcion=fila['description'],
                peliculas=fila['films']
            )
            armas.append(arma)

    return armas
