# Separar lista en dos listas, una con los elementos pares y otra con los elementos impares.

def separar_lista(lista):
    lista_pares = []
    lista_impares = []
    for elemento in lista:
        if int(elemento) % 2 == 0:
            lista_pares.append(elemento)
        else:
            lista_impares.append(elemento)
    return "Lista de pares: {} y lista de impares: {}".format(lista_pares, lista_impares)

def main_cadena_numeros():
    cadena = input("Ingrese una cadena: ")
    lista_cadena_numero = cadena.split()
    lista_cadena_numero = [int(elemento) for elemento in lista_cadena_numero]
    print(separar_lista(lista_cadena_numero))

if __name__ == "__main__":
    main_cadena_numeros()