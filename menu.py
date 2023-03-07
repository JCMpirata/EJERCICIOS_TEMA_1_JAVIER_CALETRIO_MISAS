import Ejercicio1
import Ejercicio2
import Ejercicio3
import Ejercicio4
import Ejercicio5
import Ejercicio6
import Ejercicio7

def menu():
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Ejercicio 7")
    print("8. Salir")

def main():
    while True:
        menu()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            Ejercicio1.main_voltear_cadena()
        elif opcion == 2:
            Ejercicio2.main_numero()
        elif opcion == 3:
            Ejercicio3.main_lista_comun()
        elif opcion == 4:
            Ejercicio4.main_cola()
        elif opcion == 5:
            Ejercicio5.main_numero_descomponer()
        elif opcion == 6:
            Ejercicio6.main_cadena_numeros()
        elif opcion == 7:
            Ejercicio7.main_agregar_elemento()
        elif opcion == 8:
            break
        else:
            print("Opcion incorrecta")