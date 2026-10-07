# EJERCICIO 2 - BUSCADOR DE REPUESTOS

repuestos = [
    {"codigo": "R001", "descripcion": "SSD Kingston 480 GB", "categoria": "Almacenamiento", "marca": "Kingston", "precio": 45000, "stock": 5},
    {"codigo": "R002", "descripcion": "SSD Crucial 1 TB", "categoria": "Almacenamiento", "marca": "Crucial", "precio": 65000, "stock": 3},
    {"codigo": "R003", "descripcion": "Memoria RAM 8 GB", "categoria": "Memoria", "marca": "Kingston", "precio": 28000, "stock": 0},
    {"codigo": "R004", "descripcion": "Memoria RAM 16 GB", "categoria": "Memoria", "marca": "Corsair", "precio": 50000, "stock": 4},
    {"codigo": "R005", "descripcion": "Fuente 500W", "categoria": "Fuente", "marca": "Thermaltake", "precio": 55000, "stock": 2},
    {"codigo": "R006", "descripcion": "Placa de video GTX 1650", "categoria": "Video", "marca": "MSI", "precio": 180000, "stock": 1},
    {"codigo": "R007", "descripcion": "Disco rígido 1 TB", "categoria": "Almacenamiento", "marca": "Western Digital", "precio": 60000, "stock": 0},
    {"codigo": "R008", "descripcion": "Teclado mecánico", "categoria": "Periféricos", "marca": "Redragon", "precio": 40000, "stock": 6}
]

busqueda = input("Ingrese una descripción para buscar: ").lower()

coincidencias = 0
disponibles = 0

print("\nResultados:")

for repuesto in repuestos:
    if busqueda in repuesto["descripcion"].lower():
        print(repuesto)

        coincidencias += 1

        if repuesto["stock"] > 0:
            print("Tiene stock.")
            disponibles += 1
        else:
            print("Sin stock.")

if coincidencias == 0:
    print("La búsqueda no produjo resultados.")
else:
    print("\nCantidad de coincidencias:", coincidencias)
    print("Cantidad disponibles:", disponibles)