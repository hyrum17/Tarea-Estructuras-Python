import json

# Informacion de ejemplo para guardar en formato JSON
usuario = {
    "nombre": "Estudiante",
    "habilidades": ["Python", "HTML"],
    "activo": True
}

# Guardar la informacion en datos.json
with open("datos.json", "w", encoding="utf-8") as archivo:
    json.dump(usuario, archivo, indent=4, ensure_ascii=False)

# Abrir el archivo para revisar la informacion guardada
with open("datos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    print(f"Usuario: {datos['nombre']}")
    print(f"Habilidades: {', '.join(datos['habilidades'])}")
    print(f"Activo: {datos['activo']}")
