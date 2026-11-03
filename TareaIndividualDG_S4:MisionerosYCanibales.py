import time
from collections import deque
from typing import Deque, List, Optional, Set, Tuple


Estado = Tuple[int, int, int]
Accion = Tuple[int, int]
ResultadoBusqueda = Tuple[Optional[List[Tuple[Estado, Accion]]], int]


def es_valido(estado: Estado) -> bool:
    """Determina si un estado respeta las reglas del problema."""
    misioneros, canibales, barco = estado

    if (
        misioneros < 0
        or misioneros > 3
        or canibales < 0
        or canibales > 3
        or barco not in (0, 1)
    ):
        return False

    if misioneros > 0 and misioneros < canibales:
        return False

    misioneros_derecha = 3 - misioneros
    canibales_derecha = 3 - canibales
    if (
        misioneros_derecha > 0
        and misioneros_derecha < canibales_derecha
    ):
        return False

    return True


def obtener_sucesores(estado: Estado) -> List[Tuple[Estado, Accion]]:
    """Genera los estados válidos alcanzables desde un estado dado."""
    sucesores: List[Tuple[Estado, Accion]] = []
    misioneros, canibales, barco = estado
    acciones: Tuple[Accion, ...] = ((1, 0), (2, 0), (0, 1), (0, 2), (1, 1))

    for m, c in acciones:
        if barco == 1:
            nuevo_estado = (misioneros - m, canibales - c, 0)
        else:
            nuevo_estado = (misioneros + m, canibales + c, 1)

        if es_valido(nuevo_estado):
            sucesores.append((nuevo_estado, (m, c)))

    return sucesores


def bfs(estado_inicial: Estado, estado_objetivo: Estado) -> ResultadoBusqueda:
    """Busca un camino mínimo entre dos estados usando búsqueda en anchura."""
    frontera: Deque[Tuple[Estado, List[Tuple[Estado, Accion]]]] = deque(
        [(estado_inicial, [])]
    )
    visitados: Set[Estado] = {estado_inicial}
    nodos_expandidos = 0

    while frontera:
        estado_actual, camino = frontera.popleft()

        if estado_actual == estado_objetivo:
            return camino, nodos_expandidos

        nodos_expandidos += 1

        for sucesor, accion in obtener_sucesores(estado_actual):
            if sucesor not in visitados:
                visitados.add(sucesor)
                nuevo_camino = camino + [(sucesor, accion)]
                frontera.append((sucesor, nuevo_camino))

    return None, nodos_expandidos


def dfs(estado_inicial: Estado, estado_objetivo: Estado) -> ResultadoBusqueda:
    """Busca un camino entre dos estados usando búsqueda en profundidad."""
    frontera: List[Tuple[Estado, List[Tuple[Estado, Accion]]]] = [
        (estado_inicial, [])
    ]
    visitados: Set[Estado] = {estado_inicial}
    nodos_expandidos = 0

    while frontera:
        estado_actual, camino = frontera.pop()

        if estado_actual == estado_objetivo:
            return camino, nodos_expandidos

        nodos_expandidos += 1

        for sucesor, accion in obtener_sucesores(estado_actual):
            if sucesor not in visitados:
                visitados.add(sucesor)
                nuevo_camino = camino + [(sucesor, accion)]
                frontera.append((sucesor, nuevo_camino))
    return None, nodos_expandidos

if __name__ == "__main__":
    estado_inicial = (3, 3, 1)  # 3 misioneros, 3 caníbales, barco en la orilla izquierda
    estado_objetivo = (0, 0, 0)  # Todos los misioneros y caníbales han cruzado

    inicio_bfs = time.perf_counter()
    camino_bfs, nodos_bfs = bfs(estado_inicial, estado_objetivo)
    tiempo_bfs = time.perf_counter() - inicio_bfs
    longitud_bfs = len(camino_bfs) if camino_bfs else 0

    inicio_dfs = time.perf_counter()
    camino_dfs, nodos_dfs = dfs(estado_inicial, estado_objetivo)
    tiempo_dfs = time.perf_counter() - inicio_dfs
    longitud_dfs = len(camino_dfs) if camino_dfs else 0


    print(f"{'Algoritmo':<12} | {'Nodos Expandidos':<16} | {'Tiempo (s)':<12} | {'Longitud Camino'}")
    print("-" * 65)
    print(f"{'BFS (Cola)':<12} | {nodos_bfs:<16} | {tiempo_bfs:<12.6f} | {longitud_bfs}")
    print(f"{'DFS (Pila)':<12} | {nodos_dfs:<16} | {tiempo_dfs:<12.6f} | {longitud_dfs}")
    print("-" * 65)
