# EJERCICIO 5 - SISTEMA DE CONSULTAS DE ORDENES

ordenes = [
    {
        "numero": 1001,
        "cliente": "Juan Perez",
        "equipo": "Notebook",
        "falla": "No enciende",
        "estado": "Pendiente",
        "costo": 50000
    },
    {
        "numero": 1002,
        "cliente": "Maria Lopez",
        "equipo": "PC",
        "falla": "Problema de disco",
        "estado": "En reparación",
        "costo": 75000
    },
    {
        "numero": 1003,
        "cliente": "Pedro Gomez",
        "equipo": "Notebook",
        "falla": "Pantalla rota",
        "estado": "Finalizado",
        "costo": 120000
    },
    {
        "numero": 1004,
        "cliente": "Ana Torres",
        "equipo": "PC",
        "falla": "No da imagen",
        "estado": "Pendiente",
        "costo": 60000
    },
    {
        "numero": 1005,
        "cliente": "Lucas Diaz",
        "equipo": "Notebook",
        "falla": "Teclado",
        "estado": "En reparación",
        "costo": 40000
    },
    {
        "numero": 1006,
        "cliente": "Sofia Ruiz",
        "equipo": "PC",
        "falla": "Fuente dañada",
        "estado": "Finalizado",
        "costo": 85000
    },
    {
        "numero": 1007,
        "cliente": "Mateo Silva",
        "equipo": "Notebook",
        "falla": "Batería",
        "estado": "Pendiente",
        "costo": 35000
    },
    {
        "numero": 1008,
        "cliente": "Camila Diaz",
        "equipo": "PC",
        "falla": "Sobrecalentamiento",
        "estado": "En reparación",
        "costo": 55000
    }
]


def buscar_orden(numero):
    for orden in ordenes:
        if orden["numero"] == numero:
            return orden

    return None


def filtrar_por_estado(estado):
    encontrados = 0

    for orden in ordenes:
        if orden["estado"].lower() == estado.lower():
            print(orden)
            encontrados += 1

    if encontrados == 0:
        print("No existen órdenes con ese estado.")


def filtrar_por_costo(limite):
    encontrados = 0

    for orden in ordenes:
        if orden["costo"] <= limite:
            print(orden)
            encontrados += 1

    if encontrados == 0:
        print("No existen órdenes con ese costo o menor.")


def mostrar_todas():
    for orden in ordenes:
        print(orden)


# MENÚ

while True:

    print("\n===== SISTEMA DE REPARACIONES =====")
    print("1. Buscar orden por número")
    print("2. Filtrar órdenes por estado")
    print("3. Filtrar órdenes por costo")
    print("4. Mostrar todas las órdenes")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        numero = int(input("Ingrese el número de orden: "))

        orden = buscar_orden(numero)

        if orden is not None:
            print("\nOrden encontrada:")
            print(orden)
        else:
            print("No se encontró la orden.")

    elif opcion == "2":

        estado = input("Ingrese el estado: ")

        print("\nÓrdenes encontradas:")
        filtrar_por_estado(estado)

    elif opcion == "3":

        limite = float(input("Ingrese el costo máximo: "))

        print("\nÓrdenes encontradas:")
        filtrar_por_costo(limite)

    elif opcion == "4":

        print("\nTodas las órdenes:")
        mostrar_todas()

    elif opcion == "5":

        print("Programa finalizado.")
        break

    else:
        print("Opción incorrecta.")