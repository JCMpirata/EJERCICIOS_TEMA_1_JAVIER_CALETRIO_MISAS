# Crear una estructura de tipo cola con todas las tareas ordenadas por prioridad y sin el numero de prioridad.

def ordenar_tareas(tareas):
    tareas_ordenadas = list(tareas.items())
    tareas_ordenadas.sort()
    return tareas_ordenadas

def main_cola():
    tareas = {2: "Desayunar", 4: "Comer", 1: "Hacer la cama", 3: "Ir al trabajo", 5: "Ir al gimnasio", 7: "Dormir", 6: "Cenar"}
    print(ordenar_tareas(tareas))

if __name__ == "__main__":
    main_cola()