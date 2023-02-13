
def numero_magico(numero_usuario):
    numero_magico = 12345679
    return "El resultado es: ", (numero_usuario * 9) * numero_magico

if __name__ == "__main__":
    numero_usuario = int(input("Ingrese un numero entre el 1 y el 9: "))
    print(numero_magico(numero_usuario))