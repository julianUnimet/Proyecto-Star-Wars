import funciones
import creador_de_objetos
import Mision
import registro_usuario
import sys

class App:
    def __init__(self) -> None:
        funciones.limpiar_consola()
        self.crear_objetos()    
        self.start()


    def start(self):
        """Da inicio a todas las funcionalidades del programa
        """
        self.inicio_sesion()
        
        while True:
            
            self.imprimir_menu_principal()

            #Se solicita la entrada al usuario y se verifica que sea valida
            opcion = 999
            while opcion == 999:                
                opcion = self.seleccionar_opcion([0, 1, 2, 3, 4, 5])

            #Se hace el llamado a la funcion correspondiente a la opcion seleccionada         
            if opcion == 0:
                break
            elif opcion == 1:
                self.mostrar_lista_objetos(self.peliculas, "peliculas")
            elif opcion == 2:
                self.mostrar_lista_objetos(self.especies, "seres vivos")
            elif opcion == 3:
                self.mostrar_lista_objetos(self.planetas, "planetas")
            elif opcion == 4:
                self.buscar_personaje(self.personajes) 
            elif opcion==5:
                Mision.crear_mision(self.planetas,self.naves,self.personajes,self.usuario)


    def inicio_sesion(self):
        print("1. Registrar usuario")
        print("2. Validar usuario")
        print("3. Salir")

        while True:
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                nombre_usuario = input("Ingrese el nombre de usuario: ")
                clave = input("Ingrese la clave: ")
                registro_usuario.registrar_usuario(nombre_usuario, clave)
            elif opcion == '2':
                nombre_usuario = input("Ingrese el nombre de usuario: ")
                clave = input("Ingrese la clave: ")
                if registro_usuario.validar_usuario(nombre_usuario, clave):
                    self.usuario=nombre_usuario
                    break
            elif opcion == '3':
                sys.exit()
            else:
                print("Opción no válida, intente de nuevo.")

    def imprimir_menu_principal(self):
        """Limpia la consola e Imprime en pantalla el menu principal.
        """
        funciones.limpiar_consola()
        print("BIENVENIDO A LA ENCICLOPEDIA DE STAR WARS")
        print()
        print("\t[1] Mostrar lista de peliculas")
        print("\t[2] Mostrar lista de seres vivos de la saga")
        print("\t[3] Mostrar lista de planetas")
        print("\t[4] Buscar personaje")
        print("\t[5] Crear mision")
        print("\t[0] Salir del programa")
        print()

    def seleccionar_opcion(self, opciones:list):
        """Esta funcion solicita una entrada al usuario y verifica si el valor es un int y se encuentra dentro de la lista opciones. Sirve para comprobar que la opcion ingresada por el usuario sea valida

        Args:
            opciones (list): Lista de enteros (int) que corresponden a las opciones del menu

        Returns:
            int: 999 si la ocion es invalida, si ela opcion es valida retorna el entero de la opcion
        """
        opcion = input("Inserte el numero se la opcion elegida: ")

        try:
            opcion = int(opcion)
        except:
            print(f"Ingrese una opcion valida. Es decir, cualquiera de los siguiente numeros: {opciones}")
            print()
            return 999
        
        if opcion in opciones:
            return opcion
        else:
            print(f"Ingrese una opcion valida. Es decir, cualquiera de los siguiente numeros: {opciones}")
            print()
            return 999
        
    def mostrar_lista_objetos(self, objetos:list, que_objeto_es:str):
        """Imprime en pantalla la informacion de un objeto

        Args:
            objeto (list): Lista de objetos de tipo Planeta, Especie, Pelicula o Personaje
            que_objeto_es (str): Nombre del objeto que se esta mostrando.
        """
        funciones.limpiar_consola()
        print(f"LISTA DE {que_objeto_es.upper()}")
        print()

        for i in objetos:
            i.informacion()
            print("--------------------------------------------------")
        
        print(f"En total hay {len(objetos)} {que_objeto_es}")
        print()
        input("Ingrese cualquier tecla para volver al menu anterior: ")

    
    def buscar_personaje(self, personajes:list):
        """Busca personajes

        Args:
            personajes (list): lista de todos los objetos personajes
        """
        funciones.limpiar_consola()
        
        print("BUSCAR PERSONAJE")
        print()
        nombre = input("Ingrese el nombre o parte del nombre del personaje: ")
        personajes = self.buscar_por_nombre(nombre, personajes)
        if len(personajes) == 0 :
            print("No se encontro ningun personaje con ese nombre")
        else:
            for personaje in personajes:
                personaje.informacion()
                print("--------------------------------------------------")

        input("Ingrese cualquier tecla para volver al menu anterior: ")
            

    def buscar_por_nombre(self, nombre:str, personajes:list):
        """Busca un personaje por nombre en la lista de personajes

        Args:
            nombre (str): Nombre del personaje
            personajes (list): Lista de objetos de tipo Personaje

        Returns:
            list[Personajes]: lista de objetos de tipo personaje que coinciden con el nombre o parte de el
        """
        personajes_encontrados = []

        for personaje in personajes:
            if nombre.lower() in personaje.nombre.lower():
                personajes_encontrados.append(personaje)
        
        return personajes_encontrados

    def crear_objetos(self):
        #Los metodos para crear objetos se deben llamar en este orden:
            #crear_peliculas()
            #crear_planetas()
            #crear_naves()
            #crear_vehiculos()                        
            #crear_especies()
            #crear_personajes()
            #Referenciar personajes en planetas
            #Referenciar personajes en especies
        print("Creando objetos peliculas")
        self.peliculas = creador_de_objetos.crear_peliculas()
        print("Creando objetos planetas")
        self.planetas = creador_de_objetos.crear_planetas(self.peliculas)
        print("Creando objetos naves")
        self.naves = creador_de_objetos.crear_naves()
        print("Creando objetos vehiculos")
        self.vehiculos = creador_de_objetos.crear_vehiculos()
        print("Creando objetos especies")
        self.especies = creador_de_objetos.crear_especies(self.peliculas, self.planetas)
        print("Creando objetos personajes")
        self.personajes = creador_de_objetos.crear_personajes(self.planetas, self.peliculas, self.especies, self.naves, self.vehiculos)

        #Referenciar objetos personajes en planetas
        for planeta in self.planetas:
            planeta.referenciar_personajes(self.personajes)

        #Referenciar objetos personajes en especies
        for especie in self.especies:
            especie.referenciar_personajes(self.personajes)
        

        
