# EJERCICIO 3 - CONSULTA DE ALUMNOS

alumnos = [
    {"nombre": "Lucas", "curso": "4A", "promedio": 8.5, "trabajos": 7},
    {"nombre": "Martina", "curso": "4A", "promedio": 7.2, "trabajos": 6},
    {"nombre": "Juan", "curso": "4B", "promedio": 9.1, "trabajos": 8},
    {"nombre": "Sofia", "curso": "4B", "promedio": 6.5, "trabajos": 5},
    {"nombre": "Mateo", "curso": "4A", "promedio": 8.8, "trabajos": 9},
    {"nombre": "Valentina", "curso": "4B", "promedio": 7.9, "trabajos": 7},
    {"nombre": "Tomas", "curso": "4A", "promedio": 5.8, "trabajos": 4},
    {"nombre": "Camila", "curso": "4B", "promedio": 9.5, "trabajos": 10},
    {"nombre": "Nicolas", "curso": "4A", "promedio": 6.9, "trabajos": 6},
    {"nombre": "Agustina", "curso": "4B", "promedio": 8.2, "trabajos": 8}
]

promedio_minimo = float(input("Ingrese el promedio mínimo: "))
trabajos_minimos = int(input("Ingrese la cantidad mínima de trabajos entregados: "))

cumplen = 0
no_cumplen = 0

mejor_alumno = None
mejor_promedio = 0

print("\nAlumnos que cumplen los criterios:")

for alumno in alumnos:

    if alumno["promedio"] >= promedio_minimo and alumno["trabajos"] >= trabajos_minimos:
        print(alumno["nombre"], "- Promedio:", alumno["promedio"])

        cumplen += 1

        # Buscar el mejor promedio sin usar max()
        if mejor_alumno is None or alumno["promedio"] > mejor_promedio:
            mejor_alumno = alumno
            mejor_promedio = alumno["promedio"]

    else:
        no_cumplen += 1

print("\nCantidad que cumplen:", cumplen)
print("Cantidad que no cumplen:", no_cumplen)

if mejor_alumno is not None:
    print("\nAlumno con mejor promedio:")
    print("Nombre:", mejor_alumno["nombre"])
    print("Promedio:", mejor_alumno["promedio"])
else:
    print("\nNingún alumno cumple con las condiciones.")