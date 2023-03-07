# Extraemos los elementos comunes de dos listas y que no aparezcan repetidos.

def elementos_comunes(lista1, lista2):
    lista_comun = []
    for elemento in lista1:
        if elemento in lista2:
            lista_comun.append(elemento)
            
    for elemento_comun in lista_comun:
        if lista_comun.count(elemento_comun) > 1:
            lista_comun.remove(elemento_comun)
    return lista_comun

def main_lista_comun():
    texto1 = input("Ingrese una cadena: ")
    texto2 = input("Ingrese otra cadena: ")
    lista1 = list(texto1)
    lista2 = list(texto2)
    print(elementos_comunes(lista1, lista2))
    

if __name__ == "__main__":
    main_lista_comun()

