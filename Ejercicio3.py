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

if __name__ == "__main__":
    lista1 = ["h", "o", "l", "a", " ", "m", "u", "n", "d", "o"]
    lista2 = ["h", "o", "l", "a", " ", "l", "u", "n", "a"]
    print(elementos_comunes(lista1, lista2))


