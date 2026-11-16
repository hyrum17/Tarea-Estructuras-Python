# Tarea de Estructuras de Datos - Python

Este repositorio contiene los tres ejercicios de la tarea.

## Contenido

| Archivo | Funcion |
|---|---|
| `ListaIntegrantes.py` | Agrega y elimina nombres, y guarda la lista en `roster.txt`. |
| `roster.txt` | Guarda los nombres de los integrantes. |
| `ListaNumeros.py` | Lee numeros desde `numeros.txt` y calcula la suma total. |
| `numeros.txt` | Contiene los nueve numeros del ejemplo. |
| `DatosJSON.py` | Guarda y lee informacion de un estudiante usando JSON. |
| `datos.json` | Almacena la informacion en formato JSON. |

## Requisitos
- Python 3
- Visual Studio Code (opcional)
- No se necesitan librerias externas.

## Como ejecutar
Abre una terminal en esta carpeta y ejecuta:

```bash
python ListaIntegrantes.py
python ListaNumeros.py
python DatosJSON.py
```

En Windows tambien puedes usar `py` en lugar de `python`.

## Resultados esperados
- ListaIntegrantes: muestra un menu para agregar nombres, eliminarlos o salir. Al salir, guarda la lista en `roster.txt`.
- ListaNumeros: imprime los numeros y muestra `Total: 179`.
- DatosJSON: muestra la informacion guardada en `datos.json`.

## Conceptos practicados
- Lectura y escritura de archivos de texto.
- Listas y ciclos `while` y `for`.
- Manejo de excepciones con `try` y `except`.
- Uso de `with open(...)` para cerrar archivos automaticamente.
- Uso de `json.dump()` y `json.load()`.

Los nombres y datos incluidos son ejemplos y se pueden modificar segun las indicaciones del profesor.
