import json


def guardar_red(grafo, archivo):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(grafo, f, indent=4, ensure_ascii=False)

    print("Red guardada correctamente.")


def cargar_red(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            grafo = json.load(f)

        print("Red cargada correctamente.")
        return grafo

    except FileNotFoundError:
        print("No se encontró el archivo. Se empezará con una red vacía.")
        return {}