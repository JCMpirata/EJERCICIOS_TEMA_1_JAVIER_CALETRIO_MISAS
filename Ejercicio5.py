# Descomponer un numero entero en unidades, decenas, centenas, etc.

def descomponer(numero):
    unidades = numero % 10
    decenas = (numero % 100) // 10
    centenas = (numero % 1000) // 100
    miles = (numero % 10000) // 1000
    return "Unidades: {}, Decenas: {}, Centenas: {}, Miles: {}".format(unidades, decenas, centenas, miles)

def main_numero_descomponer():
    numero = int(input("Ingrese un numero entero: "))
    print(descomponer(numero))

if __name__ == "__main__":
    main_numero_descomponer()