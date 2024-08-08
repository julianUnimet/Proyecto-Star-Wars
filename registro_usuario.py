import hashlib
import os

def registrar_usuario(nombre_usuario, clave):
    """Registra un usuario con una clave en un archivo de texto.

    Args:
        nombre_usuario (str): El nombre del usuario.
        clave (str): La clave del usuario.

    Returns:
        bool: True si el registro fue exitoso, False si el usuario ya existe.
    """
    archivo_usuarios = 'usuarios.txt'

    if os.path.exists(archivo_usuarios):
        with open(archivo_usuarios, 'r') as file:
            for linea in file:
                usuario, _ = linea.strip().split(',')
                if usuario == nombre_usuario:
                    print("El usuario ya existe.")
                    return False

    # Hashear la clave
    clave_hash = hashlib.sha256(clave.encode()).hexdigest()

    with open(archivo_usuarios, 'a') as file:
        file.write(f'{nombre_usuario},{clave_hash}\n')

    print("Usuario registrado exitosamente.")
    return True

def validar_usuario(nombre_usuario, clave):
    """Valida un usuario con su clave.

    Args:
        nombre_usuario (str): El nombre del usuario.
        clave (str): La clave del usuario.

    Returns:
        bool: True si la validación fue exitosa, False en caso contrario.
    """
    archivo_usuarios = 'usuarios.txt'

    if not os.path.exists(archivo_usuarios):
        print("No hay usuarios registrados.")
        return False

    clave_hash = hashlib.sha256(clave.encode()).hexdigest()

    with open(archivo_usuarios, 'r') as file:
        for linea in file:
            usuario, clave_almacenada = linea.strip().split(',')
            if usuario == nombre_usuario and clave_almacenada == clave_hash:
                print("Usuario validado exitosamente.")
                return True

    print("Nombre de usuario o clave incorrectos.")
    return False
