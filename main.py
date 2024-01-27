# archivo main ejecucion del programa
from interprete import comandos_basicos

menu=True

while menu :
        comandos = input("> ")

        if comandos.lower() == "quit":
            menu = False
            print("programa terminado ")
        else:
            comandos_basicos(comandos)

