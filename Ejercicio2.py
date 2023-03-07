
def numero_magico(numero_usuario):
    numero_magico = 12345679
    return "El resultado es: {}".format((numero_usuario * 9) * numero_magico)

def main_numero():
    numero_usuario = int(input("Ingrese un numero del 1 al 9 incluidos: "))
    if numero_usuario >= 1 and numero_usuario <= 9:
        print(numero_magico(numero_usuario))
    else:
        print("El numero no esta dentro del rango")


if __name__ == "__main__":
    main_numero()