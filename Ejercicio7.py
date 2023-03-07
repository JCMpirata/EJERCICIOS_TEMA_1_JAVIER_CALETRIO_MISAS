# Agregar elementos una vez a una lista dada, sin repetirlos. Si el elemento ya existe, 
# invocar un error de tipo ValueError.

def agregar_elemento(lista, elemento):
    if elemento in lista:
        raise ValueError("El elemento ya existe en la lista")
    else:
        lista.append(elemento)
    return lista

def main_agregar_elemento():
    lista = ["1", "5", "-2"]
    elemento = input("Ingrese un elemento: ")
    print(agregar_elemento(lista, elemento))

if __name__ == "__main__":
    main_agregar_elemento()