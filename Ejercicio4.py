# Crear una estructura de tipo cola con todas las tareas ordenadas por prioridad y sin el numero de prioridad.

def ordenar_tareas(tareas):
    tareas_ordenadas = []
    for tarea in tareas:
        tareas_ordenadas.append(tarea[2:])
    return tareas_ordenadas

if __name__ == "__main__":
    tareas = ["2. Hacer la cama", "4. Hacer la comida", "1. Hacer la cena", "3. Hacer la tarea"]
    print(ordenar_tareas(tareas))