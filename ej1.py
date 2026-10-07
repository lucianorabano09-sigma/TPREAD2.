# EJERCICIO 1 - CONTROL DEL LABORATORIO

inventario = [
    {"inventario": 1, "tipo": "PC", "marca": "HP", "estado": "Disponible", "año": 2022},
    {"inventario": 2, "tipo": "Notebook", "marca": "Lenovo", "estado": "En reparación", "año": 2021},
    {"inventario": 3, "tipo": "PC", "marca": "Dell", "estado": "Disponible", "año": 2023},
    {"inventario": 4, "tipo": "Monitor", "marca": "Samsung", "estado": "Baja", "año": 2019},
    {"inventario": 5, "tipo": "Notebook", "marca": "Acer", "estado": "Disponible", "año": 2024},
    {"inventario": 6, "tipo": "PC", "marca": "Lenovo", "estado": "Disponible", "año": 2020},
    {"inventario": 7, "tipo": "Monitor", "marca": "LG", "estado": "En reparación", "año": 2022},
    {"inventario": 8, "tipo": "Notebook", "marca": "HP", "estado": "Disponible", "año": 2023}
]

año_minimo = int(input("Ingrese el año mínimo: "))

cantidad = 0

print("\nEquipos disponibles que cumplen la condición:")

# Un único recorrido de la lista
for equipo in inventario:
    if equipo["estado"] == "Disponible" and equipo["año"] >= año_minimo:
        print(equipo)
        cantidad += 1

if cantidad == 0:
    print("No hay equipos disponibles que cumplan con las condiciones.")
else:
    print("Cantidad de equipos que cumplen:", cantidad)