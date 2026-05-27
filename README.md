# FINAL--Estructura-de-Datos-y-Algoritmos
Parte 2: Codigo
# Planificador de Rutas en una Red de Transporte

## Descripción

Este proyecto implementa un planificador de rutas usando una red de transporte representada mediante un grafo ponderado. Cada estación representa un nodo y cada conexión entre estaciones tiene asociado un tiempo en minutos.

El programa permite:

- Añadir estaciones.
- Añadir conexiones entre estaciones.
- Mostrar la red completa.
- Buscar la ruta más rápida entre dos estaciones.
- Buscar la ruta más rápida pasando obligatoriamente por una estación intermedia.
- Guardar y cargar la red desde un archivo JSON.
- Reiniciar completamente la red.

---

 Estructura de datos utilizada
La red se representa mediante un diccionario de diccionarios funcionando como una lista de adyacencia.

Cada clave principal representa una estación y dentro se almacenan sus conexiones junto con el tiempo asociado.

Esta estructura permite acceder rápidamente a las conexiones de cada estación.

#Persistencia 
La persistencia se implementa usando archivos JSON.

##Complejidad Temporal
#Añadir estación
O(1): porque insertar en un diccionario es una operación constante promedio.

#Añadir conexión
O(1) : porque simplemente se añaden entradas al diccionario.
#Mostrar red
O(V + E)


#Complejidad Espacial
O(V + E): ya que se almacenan todas las estaciones y conexiones.


Posibles Mejoras
Eliminar estaciones y conexiones.
Permitir conexiones en un solo sentido.
Añadir interfaz gráfica.
Dibujar visualmente el grafo.
Separar el código en varios archivos para mejorar modularidad.
Optimizar memoria usando predecesores en lugar de guardar rutas completas.
Añadir diferentes medios de transporte y costos adicionales.
