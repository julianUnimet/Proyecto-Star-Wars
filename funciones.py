import os

#Biblioteca de funciones variadas

def limpiar_consola():
    """Limpia la consola tanto en windows como en linux
    """
    if os.name =="nt": #Para Wiondows
        os.system("cls")
    else: 
        os.system("clear")

