# EJERCICIO 6 - POO: CATALOGO DE DISPOSITIVOS DE RED


class DispositivoRed:

    def __init__(self, codigo, tipo, marca, velocidad_mbps, precio, stock):
        self.codigo = codigo
        self.tipo = tipo
        self.marca = marca
        self.velocidad_mbps = velocidad_mbps
        self.precio = precio
        self.stock = stock

    def mostrar_datos(self):
        print("Código:", self.codigo)
        print("Tipo:", self.tipo)
        print("Marca:", self.marca)
        print("Velocidad:", self.velocidad_mbps, "Mbps")
        print("Precio: $", self.precio)
        print("Stock:", self.stock)
        print("-------------------------")

    def hay_stock(self):
        if self.stock > 0:
            return True
        else:
            return False


# Crear dispositivos

dispositivos = [
    DispositivoRed("D001", "Router", "TP-Link", 300, 35000, 5),
    DispositivoRed("D002", "Router", "TP-Link", 1200, 70000, 3),
    DispositivoRed("D003", "Switch", "Cisco", 1000, 90000, 2),
    DispositivoRed("D004", "Access Point", "Ubiquiti", 1200, 110000, 0),
    DispositivoRed("D005", "Switch", "D-Link", 1000, 60000, 4),
    DispositivoRed("D006", "Router", "Mikrotik", 2500, 150000, 1)
]


# Buscar dispositivos por velocidad

def buscar_por_velocidad(velocidad_minima):

    encontrados = 0

    for dispositivo in dispositivos:
        if dispositivo.velocidad_mbps >= velocidad_minima and dispositivo.hay_stock():
            dispositivo.mostrar_datos()
            encontrados += 1

    if encontrados == 0:
        print("No hay dispositivos que cumplan las condiciones.")


# Buscar dispositivo por código

def buscar_por_codigo(codigo):

    for dispositivo in dispositivos:
        if dispositivo.codigo.lower() == codigo.lower():
            return dispositivo

    return None


# Mostrar dispositivos según presupuesto

def buscar_por_presupuesto(presupuesto):

    encontrados = 0

    for dispositivo in dispositivos:

        if dispositivo.hay_stock() and dispositivo.precio <= presupuesto:
            dispositivo.mostrar_datos()
            encontrados += 1

    if encontrados == 0:
        print("No hay dispositivos disponibles dentro del presupuesto.")


# PROGRAMA PRINCIPAL

print("===== CATÁLOGO DE DISPOSITIVOS DE RED =====")

# Consulta por velocidad

velocidad = int(input("\nIngrese la velocidad mínima en Mbps: "))

print("\nDispositivos con esa velocidad o superior y con stock:")
buscar_por_velocidad(velocidad)


# Consulta por código

codigo = input("\nIngrese un código para buscar: ")

dispositivo = buscar_por_codigo(codigo)

if dispositivo is not None:
    print("\nDispositivo encontrado:")
    dispositivo.mostrar_datos()
else:
    print("No se encontró ningún dispositivo con ese código.")


# Consulta por presupuesto

presupuesto = float(input("\nIngrese su presupuesto máximo: "))

print("\nDispositivos que puede comprar:")
buscar_por_presupuesto(presupuesto)