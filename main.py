from App import App
import registro_usuario
import sys

def inicio_sesion():
    print("1. Registrar usuario")
    print("2. Validar usuario")
    print("3. Salir")

if __name__ == "__main__":
    while True:
        inicio_sesion()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre_usuario = input("Ingrese el nombre de usuario: ")
            clave = input("Ingrese la clave: ")
            registro_usuario.registrar_usuario(nombre_usuario, clave)
        elif opcion == '2':
            nombre_usuario = input("Ingrese el nombre de usuario: ")
            clave = input("Ingrese la clave: ")
            if registro_usuario.validar_usuario(nombre_usuario, clave):
                break
        elif opcion == '3':
            sys.exit()
        else:
            print("Opción no válida, intente de nuevo.")

def main():
    inicio_sesion()
    app = App()

if __name__ =="__main__":
    main()