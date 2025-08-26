# 🧩 Programación III - Trabajos Prácticos

Este repositorio contiene la resolución de los **Trabajos Prácticos de
Programación III** correspondientes a la **Tecnicatura Universitaria en
Inteligencia Artificial (FCEIA - UNR)**, realizados durante el **segundo
cuatrimestre de 2023** por **Texier Julieta** y **Masciángelo Lucía**.

El objetivo principal de estos trabajos es **implementar distintos
algoritmos de búsqueda y optimización**, tanto en espacios de estados
como en problemas combinatorios, aplicando conceptos de estructuras de
datos, heurísticas y visualización.

------------------------------------------------------------------------

## 📌 TP-Pathfinding

### Objetivo

Implementar distintos algoritmos de búsqueda para resolver laberintos,
visualizando el proceso y comparando resultados.

### Algoritmos implementados

-   **BFS (Breadth-First Search)**\
-   **DFS (Depth-First Search)**\
-   **UCS (Uniform Cost Search)**\
-   **GBFS (Greedy Best-First Search)**\
-   **A**\*\
-   **Go Right** (algoritmo base provisto)

### Archivos principales

-   `bfs.py`, `dfs.py`, `ucs.py`, `gbfs.py`, `astar.py` →
    Implementaciones de los algoritmos.\
-   `goright.py` → Algoritmo de ejemplo provisto.\
-   `enunciado.pdf` → Consigna completa y explicación de las clases de
    apoyo.

### Clases de apoyo (provistas por la cátedra)

-   **Node**, **Grid**, **Frontier** (Pila, Cola, Cola de Prioridad).\
-   **Solution / NoSolution** para representar el resultado.

### Ejecución

1.  Clonar el repositorio base de la cátedra (si corresponde):

    ``` bash
    git clone https://github.com/maurolucci/tuia-prog3.git
    pip install -r requirements.txt
    ```

2.  Copiar los archivos de este TP en `src/pathfinder/search/`.\

3.  Ejecutar:

    ``` bash
    python3 run.pyw
    ```

4.  Desde la interfaz seleccionar algoritmo, generar o dibujar laberinto
    y visualizar.

------------------------------------------------------------------------

## 📌 TP-TSP (Traveling Salesman Problem)

### Objetivo

Implementar y comparar distintos **algoritmos de búsqueda local** para
resolver el problema del viajante de comercio (TSP).

### Algoritmos implementados

1.  **Hill Climbing**
    -   Búsqueda de mejoras locales, moviéndose siempre hacia el sucesor
        con mejor valor.\
2.  **Random Restart Hill Climbing**
    -   Variante con reinicios aleatorios para evitar óptimos locales.\
3.  **Tabu Search**
    -   Utiliza una lista tabú para recordar movimientos recientes y
        explorar más ampliamente el espacio de soluciones.

### Archivos principales

-   `search.py` → Contiene la clase base `LocalSearch` y las
    implementaciones de:
    -   `HillClimbing` (provisto)\
    -   `HillClimbingReset` (implementado por nosotras)\
    -   `Tabu` (implementado por nosotras)\
-   `enunciado.pdf` → Consigna completa, explicación del problema y
    clases de apoyo.

### Clases y conceptos clave

-   **OptProblem / TSP**: Representan el problema, estado inicial,
    función objetivo, acciones (2-opt).\
-   **LocalSearch**: Clase base con atributos como `tour`, `value`,
    `niters`, `time`.\
-   **Acciones 2-opt**: Intercambio de aristas para generar vecinos.

### Ejecución

1.  Clonar el repositorio base de la cátedra:

    ``` bash
    git clone https://github.com/maurolucci/tuia-prog3.git
    pip install -r requirements.txt
    ```

2.  Copiar `search.py` y demás archivos de este TP en la carpeta
    correspondiente.\

3.  Ejecutar el programa principal sobre una instancia TSP:

    ``` bash
    python3 main.py instances/ar24.tsp
    ```

4.  Visualizar en consola las métricas y en la interfaz gráfica las
    soluciones obtenidas por cada algoritmo.

### Resultados

-   Comparación de soluciones encontradas, tiempos de ejecución e
    iteraciones para cada algoritmo.\
-   Observación del impacto de los reinicios aleatorios y la lista tabú
    en la calidad de las soluciones.

------------------------------------------------------------------------

## 🛠 Tecnologías utilizadas

-   **Python 3.10+**\
-   **Programación orientada a objetos**\
-   **Estructuras de datos personalizadas**\
-   **Visualización gráfica provista por la cátedra**

------------------------------------------------------------------------

## ✨ Autoras

**Julieta Texier**\
**Lucía Masciángelo**\
*Tecnicatura Universitaria en Inteligencia Artificial - FCEIA - UNR*\
*Segundo cuatrimestre 2023*
