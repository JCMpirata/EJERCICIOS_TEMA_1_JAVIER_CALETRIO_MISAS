
def voltear_cadena(cadena):
    cadena_volteada = cadena[::-1]
    for cadena_separada in cadena_volteada:
        cadena_separada = cadena_volteada.split(" ")
        return "{} {} ha sacado un {} de nota".format(cadena_separada[1], cadena_separada[2], cadena_separada[0])
    
def main_voltear_cadena():
    cadena = input("Ingrese una cadena: ")
    print(voltear_cadena(cadena))
    
if __name__ == "__main__":
    main_voltear_cadena()