import Ejercicio1
import Ejercicio2
import Ejercicio3
import Ejercicio4
import Ejercicio5
import Ejercicio6
import Ejercicio7

def menu_iniciar():
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Ejercicio 7")
    print("8. Salir")

    while True:
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            print("Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?")
            Ejercicio1.main_voltear_cadena()

        elif opcion == 2:
            print("Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación.")
            Ejercicio2.main_numero()

        elif opcion == 3:
            print("Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista")
            Ejercicio3.main_lista_comun()

        elif opcion == 4:
            print("Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).")
            Ejercicio4.main_cola()

        elif opcion == 5:
            print("Crea un script llamado descomposicion.py que realice las siguientes tareas:")
            print("Debe tomar 1 argumento que será un número entero positivo.")
            print("En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.")
            print("El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... ")
            Ejercicio5.main_numero_descomponer()

        elif opcion == 6:
            print("Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.")
            Ejercicio6.main_cadena_numeros()

        elif opcion == 7:
            print("Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:")
            print("Error: Imposible añadir elementos duplicados => [elemento].")
            Ejercicio7.main_agregar_elemento()

        elif opcion == 8:
            break
        
        else:
            print("Opcion incorrecta")