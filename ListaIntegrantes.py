# Programa para administrar una lista de integrantes
# Los nombres se guardan en roster.txt para conservarlos al cerrar.

archivo_roster = "roster.txt"
roster = []

# Leer los nombres que ya existen en el archivo
try:
    with open(archivo_roster, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre = linea.strip()
            if nombre:
                roster.append(nombre)
except FileNotFoundError:
    print("Creando archivo para la lista.")

while True:
    print("\nLista:", roster)
    print("1. Agregar Nombre")
    print("2. Eliminar Nombre")
    print("3. Salir")

    try:
        eleccion = int(input("Seleccion: "))
    except ValueError:
        print("Escribe 1, 2 o 3.")
        continue

    if eleccion == 1:
        nuevo_nombre = input("Nombre: ").strip()
        if nuevo_nombre:
            roster.append(nuevo_nombre)
            print("Nombre agregado.")
        else:
            print("El nombre no puede estar vacio.")

    elif eleccion == 2:
        nombre_eliminar = input("Eliminar: ").strip()
        try:
            roster.remove(nombre_eliminar)
            print("Nombre eliminado.")
        except ValueError:
            print("Error al eliminar: el nombre no esta en la lista.")

    elif eleccion == 3:
        break

    else:
        print("Opcion no valida.")

# Guardar todos los nombres antes de terminar
with open(archivo_roster, "w", encoding="utf-8") as archivo:
    for nombre in roster:
        archivo.write(nombre + "\n")

print("Lista guardada correctamente.")
