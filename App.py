import funciones
import creador_de_objetos

class App:
    def __init__(self) -> None:
        funciones.limpiar_consola()
        self.crear_objetos()
        self.start()


    def start(self):
        """Da inicio a todas las funcionalidades del programa
        """
        
        
        while True:
            self.imprimir_menu_principal()

            #Se solicita la entrada al usuario y se verifica que sea valida
            opcion = 999
            while opcion == 999:                
                opcion = self.seleccionar_opcion([0, 1, 2, 3, 4])

            #Se hace el llamado a la funcion correspondiente a la opcion seleccionada         
            if opcion == 0:
                break
            elif opcion == 1:
                self.mostrar_lista_peliculas([])
            elif opcion == 2:
                self.mostrar_lista_seres_vivos([])
            elif opcion == 3:
                self.mostrar_lista_planetas([])
            elif opcion == 4:
                self.buscar_personaje("")



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

    def mostrar_lista_peliculas(self, peliculas:list):
        funciones.limpiar_consola()
        for i in self.peliculas:
            i.informacion()
            print("--------------------------------------------------")

        input("Ingrese cualquier tecla para volver al menu anterior: ") 

    def mostrar_lista_seres_vivos(self, seres_vivos:list):
        funciones.limpiar_consola()
        for i in self.especies:
            i.informacion()
            print("--------------------------------------------------")
        
        print(f"En total hay {len(self.especies)} especies")
        print()
        input("Ingrese cualquier tecla para volver al menu anterior: ") 

    def mostrar_lista_planetas(self, planetas:list):
        pass

    def buscar_personaje(self,nombre_o_id, personajes:list):
        #revisar si es necesaria la busqueda por id o si solo se necesita por nombre
        #se puede hacer una busqueda de las dos formas revisando si el parametro es un entero o no
        pass

    def crear_objetos(self):
        self.peliculas = creador_de_objetos.crear_peliculas()
        self.especies = creador_de_objetos.crear_especies()

#Este llamado esta aqui para probar el codigo, luego este llamado se debe hacer desde main.py     
#app = App()