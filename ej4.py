# EJERCICIO 4 - VERSION CORREGIDA

libros = [
    {"isbn": "111", "titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "disponible": True},
    {"isbn": "222", "titulo": "1984", "autor": "George Orwell", "disponible": False},
    {"isbn": "333", "titulo": "Harry Potter", "autor": "J.K. Rowling", "disponible": True},
    {"isbn": "444", "titulo": "Dracula", "autor": "Bram Stoker", "disponible": True},
    {"isbn": "555", "titulo": "Frankenstein", "autor": "Mary Shelley", "disponible": False}
]

isbn_buscar = input("Ingrese el ISBN: ")

encontrado = False

for libro in libros:
    if libro["isbn"] == isbn_buscar:
        print("\nLibro encontrado:")
        print("ISBN:", libro["isbn"])
        print("Título:", libro["titulo"])
        print("Autor:", libro["autor"])
        print("Disponible:", libro["disponible"])

        encontrado = True
        break

if encontrado == False:
    print("Libro no encontrado")