import json
import heapq


archivo = "red_transporte.json"


class RedTransporte:
    def __init__(self):
        self.grafo = {}

    def anadir_estacion(self, estacion):
        if estacion not in self.grafo:
            self.grafo[estacion] = {}
            print("Estación añadida correctamente.")
        else:
            print("Esa estación ya existe.")

    def anadir_conexion(self, origen, destino, minutos):
        if origen not in self.grafo:
            self.anadir_estacion(origen)

        if destino not in self.grafo:
            self.anadir_estacion(destino)

        self.grafo[origen][destino] = minutos
        self.grafo[destino][origen] = minutos

        print("Conexión añadida correctamente.")

    def mostrar_red(self):
        if not self.grafo:
            print("La red está vacía.")
            return

        for estacion, conexiones in self.grafo.items():
            print(f"\n{estacion}:")
            for destino, minutos in conexiones.items():
                print(f"  -> {destino}: {minutos} min")

    def dijkstra(self, origen, destino):
        if origen not in self.grafo or destino not in self.grafo:
            return None

        cola = []
        heapq.heappush(cola, (0, origen, [origen]))

        visitados = set()

        while cola:
            tiempo_actual, estacion_actual, ruta = heapq.heappop(cola)

            if estacion_actual in visitados:
                continue

            visitados.add(estacion_actual)

            if estacion_actual == destino:
                return tiempo_actual, ruta

            for vecino, minutos in self.grafo[estacion_actual].items():
                if vecino not in visitados:
                    nuevo_tiempo = tiempo_actual + minutos
                    nueva_ruta = ruta + [vecino]
                    heapq.heappush(cola, (nuevo_tiempo, vecino, nueva_ruta))

        return None

    def guardar_red(self):
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(self.grafo, f, indent=4, ensure_ascii=False)
        print("Red guardada correctamente.")

    def cargar_red(self):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                self.grafo = json.load(f)
            print("Red cargada correctamente.")
        except FileNotFoundError:
            print("No se encontró el archivo. Se empezará con una red vacía.")

    def reiniciar_red(self):
        self.grafo = {}
        print("Red reiniciada correctamente.")


red = RedTransporte()

#MENU PRINCIPAL 
while True:
    print("\n" + "~" * 30)
    print("PLANIFICADOR DE RUTAS")
    print("~" * 30)

    print("1. Cargar Red Desde Archivo")
    print("2. Anadir Estacion")
    print("3. Anadir Conexion")
    print("4. Mostrar Estaciones y Conexiones")
    print("5. Buscar Ruta Mas Rapida")
    print("6. Guardar y Salir")
    print("7. Reiniciar Red")
          

    opcion = input("Elige una opción: ")

    if opcion == "1":
        red.cargar_red()

    elif opcion == "2":
        estacion = input("Nombre de la estación: ")
        red.anadir_estacion(estacion)

    elif opcion == "3":
        origen = input("Estación origen: ")
        destino = input("Estación destino: ")
        minutos = int(input("Tiempo en minutos: "))

        red.anadir_conexion(origen, destino, minutos)

    elif opcion == "4":
        red.mostrar_red()

    elif opcion == "5":
        origen = input("Origen: ")
        destino = input("Destino: ")

        resultado = red.dijkstra(origen, destino)

        if resultado is None:
            print("No se encontró una ruta.")
        else:
            tiempo, ruta = resultado
            print("Ruta más rápida:", " -> ".join(ruta))
            print("Tiempo total:", tiempo, "minutos")

    elif opcion == "6":
        red.guardar_red()
        print("Saliendo del programa...")
        break

    elif opcion == "7":
        red.reiniciar_red()

    else:
        print("Opción no válida.")