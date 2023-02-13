# Separar lista en dos listas, una con los elementos pares y otra con los elementos impares.

def separar_lista(lista):
    lista_pares = []
    lista_impares = []
    for elemento in lista:
        if int(elemento) % 2 == 0:
            lista_pares.append(elemento)
        else:
            lista_impares.append(elemento)
    return f"Pares: {lista_pares}", f" Impares: {lista_impares}"

if __name__ == "__main__":
    lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print(separar_lista(lista))