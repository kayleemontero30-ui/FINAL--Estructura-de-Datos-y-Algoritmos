import heapq


class Grafo:
    def __init__(self):
        self.red = {}

    def anadir_estacion(self, estacion):
        if estacion not in self.red:
            self.red[estacion] = {}
            print("Estación añadida correctamente.")
        else:
            print("Esa estación ya existe.")

    def anadir_conexion(self, origen, destino, minutos):
        if origen not in self.red:
            self.anadir_estacion(origen)

        if destino not in self.red:
            self.anadir_estacion(destino)

        self.red[origen][destino] = minutos
        self.red[destino][origen] = minutos

        print("Conexión añadida correctamente.")

    def mostrar_red(self):
        if not self.red:
            print("La red está vacía.")
            return

        for estacion, conexiones in self.red.items():
            print(f"\n{estacion}:")
            for destino, minutos in conexiones.items():
                print(f"  -> {destino}: {minutos} min")

    def dijkstra(self, origen, destino):
        if origen not in self.red or destino not in self.red:
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

            for vecino, minutos in self.red[estacion_actual].items():
                if vecino not in visitados:
                    nuevo_tiempo = tiempo_actual + minutos
                    nueva_ruta = ruta + [vecino]
                    heapq.heappush(cola, (nuevo_tiempo, vecino, nueva_ruta))

        return None

    def reiniciar_red(self):
        self.red = {}
        print("Red reiniciada correctamente.")