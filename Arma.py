class Arma:
    """
    Clase que representa un arma en el universo de Star Wars.

    Atributos:
        id (int): Identificador único del arma.
        nombre (str): Nombre del arma.
        modelo (str): Modelo del arma.
        fabricante (str): Fabricante del arma.
        costo_en_creditos (float): Costo del arma en créditos galácticos.
        longitud (float): Longitud del arma en metros.
        tipo (str): Tipo de arma (e.g., Melee, Blaster).
        descripcion (str): Descripción del arma.
        peliculas (list): Lista de películas en las que aparece el arma.
    """

    def __init__(self, id, nombre, modelo, fabricante, costo_en_creditos, longitud, tipo, descripcion, peliculas):
        """
        Inicializa un objeto Arma con los atributos especificados.

        Args:
            id (int): Identificador único del arma.
            nombre (str): Nombre del arma.
            modelo (str): Modelo del arma.
            fabricante (str): Fabricante del arma.
            costo_en_creditos (float): Costo del arma en créditos galácticos.
            longitud (float): Longitud del arma en metros.
            tipo (str): Tipo de arma (e.g., Melee, Blaster).
            descripcion (str): Descripción del arma.
            peliculas (str): Cadena de texto con las películas en las que aparece el arma.
        """
        self.id = id
        self.nombre = nombre
        self.modelo = modelo
        self.fabricante = fabricante
        self.costo_en_creditos = float(costo_en_creditos) if costo_en_creditos else None
        self.longitud = float(longitud) if longitud else None
        self.tipo = tipo
        self.descripcion = descripcion
        self.peliculas = peliculas.split(', ')  # Convertir la cadena de películas en una lista

    def __str__(self):
        """
        Retorna una cadena de texto que describe el arma.

        Returns:
            str: Descripción del arma con sus atributos principales.
        """
        return (f"Arma: {self.nombre}\n"
                f"  Modelo: {self.modelo}\n"
                f"  Fabricante: {self.fabricante}\n"
                f"  Costo: {self.costo_en_creditos} créditos\n"
                f"  Longitud: {self.longitud} metros\n"
                f"  Tipo: {self.tipo}\n"
                f"  Descripción: {self.descripcion}\n"
                f"  Películas: {', '.join(self.peliculas)}\n")