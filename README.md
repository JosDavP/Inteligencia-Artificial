# Inteligencia-Artificial
Talleres, practicas y laboratorios individuales del curso de Inteligencia Artificial con el prof. David Galarza
## Tarea Individual DG_S4: Formulación y Búsqueda Ciega en Espacios de Estados
Este proyecto contiene la formulación matemática y la implementación en Python del clásico problema de Inteligencia Artificial de los Misioneros y Caníbales. El objetivo del script es modelar el espacio de estados y resolver el problema utilizando algoritmos de búsqueda no informada, garantizando que en ninguna orilla los caníbales superen en número a los misioneros.

### Características Principales:

Modelado de Estados: Representación matemática mediante tuplas (M, C, B) que indican la cantidad de misioneros, caníbales y la posición del bote en la orilla de origen.

Algoritmos Implementados: Búsqueda en Anchura (BFS) utilizando estructuras FIFO (colas) y Búsqueda en Profundidad (DFS) utilizando estructuras LIFO (pilas).

Benchmarking Empírico: Módulo de evaluación automatizado que ejecuta ambos algoritmos y genera una tabla comparativa detallando el número de nodos expandidos, el tiempo de ejecución (en segundos) y la longitud del camino óptimo encontrado.
