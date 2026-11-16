# Leer numeros desde numeros.txt y calcular la suma total

try:
    suma = 0

    # Abrir el archivo y leer cada numero
    with open("numeros.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # Quitar espacios y saltos de linea antes de convertir
            numero = int(linea.strip())
            print(numero)
            suma += numero

    print(f"Total: {suma}")

except FileNotFoundError:
    print("No se encontro el archivo numeros.txt.")
except ValueError as error:
    print(f"Hay una linea que no contiene un numero entero: {error}")
