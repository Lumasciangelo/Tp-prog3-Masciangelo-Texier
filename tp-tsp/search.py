"""Este modulo define la clase LocalSearch.

LocalSearch representa un algoritmo de busqueda local general.

Las subclases que se encuentran en este modulo son:

* HillClimbing: algoritmo de ascension de colinas. Se mueve al sucesor con
mejor valor objetivo, y los empates se resuelvan de forma aleatoria.
Ya viene implementado.

* HillClimbingReset: algoritmo de ascension de colinas de reinicio aleatorio.
No viene implementado, se debe completar.

* Tabu: algoritmo de busqueda tabu.
No viene implementado, se debe completar.
"""


from __future__ import annotations
from problem import OptProblem, TSP
from random import choice
from time import time


class LocalSearch:
    """Clase que representa un algoritmo de busqueda local general."""

    def __init__(self) -> None:
        """Construye una instancia de la clase."""
        self.niters = 0  # Numero de iteraciones totales
        self.time = 0  # Tiempo de ejecucion
        self.tour = []  # Solucion, inicialmente vacia
        self.value = None  # Valor objetivo de la solucion

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion."""
        self.tour = problem.init
        self.value = problem.obj_val(problem.init)


class HillClimbing(LocalSearch):
    """Clase que representa un algoritmo de ascension de colinas.

    En cada iteracion se mueve al estado sucesor con mejor valor objetivo.
    El criterio de parada es alcanzar un optimo local.
    """

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        value = problem.obj_val(problem.init)

        while True:

            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual)

            # Buscar las acciones que generan el mayor incremento de valor obj
            max_acts = [act for act, val in diff.items() if val ==
                        max(diff.values())]

            # Elegir una accion aleatoria
            act = choice(max_acts)

            # Retornar si estamos en un optimo local 
            # (diferencia de valor objetivo no positiva)
            if diff[act] <= 0:

                self.tour = actual
                self.value = value
                end = time()
                self.time = end-start
                return

            # Sino, nos movemos al sucesor
            else:

                actual = problem.result(actual, act)
                value = value + diff[act]
                self.niters += 1


class HillClimbingReset(LocalSearch):
    """Algoritmo de ascension de colinas con reinicio aleatorio."""

    def solve(self, problem: TSP):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        value = problem.obj_val(problem.init)

        #Definimos estos dos valores para usarlos en el random reset
        self.value = float('-inf')
        n = 10

        while True:

            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual)

            # Buscar las acciones que generan el mayor incremento de valor obj
            max_acts = [act for act, val in diff.items() if val ==
                        max(diff.values())]

            # Elegir una accion aleatoria
            act = choice(max_acts)

            # Retornar si estamos en un optimo local 
            # (diferencia de valor objetivo no positiva)
        
            if diff[act] <= 0:
               n-= 1
               #primero nos fijamos si es mayor al self.tour que tengo guardado
               if self.value < value:
                    self.tour = actual
                    self.value = value
               #si no me quedo con lo que tenia
               #ahora reseteo si n es mayor a 0
               if n > 0:
                    actual = problem.random_reset()
                    value = problem.obj_val(actual)
                     
               else: 
                    end = time()
                    self.time = end-start
                    return

            # Sino, nos movemos al sucesor
            else:

                actual = problem.result(actual, act)
                value = value + diff[act]
                self.niters += 1


class Tabu(LocalSearch):
    """Algoritmo de busqueda tabu."""
    def solve(self, problem: OptProblem):

        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        state_mejor = actual
        value_mejor = problem.obj_val(problem.init)
        lista_tabu = []

        # El criteriode parada que elegimos es la cantidad de iteriaciones
        while self.niters < 700:

            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual)

            no_tabues = {}

            for i,j in diff.items():
                if i not in lista_tabu:
                    no_tabues[i] = j

            # Buscar las acciones que generan el mayor incremento de valor obj
            max_acts = [act for act, val in no_tabues.items() if val ==
                        max(no_tabues.values())]

            # Elegir una accion aleatoria
            act = choice(max_acts)

            # Nos movemos al sucesor
            actual = problem.result(actual, act)
            value = problem.obj_val(actual)
            
            # La cantidad de valores lo decidimos comparando diversos numeros
            if len(lista_tabu) > 40:
                lista_tabu.pop(0)
            
            lista_tabu.append(act)
            self.niters += 1
            if value_mejor < value:
                state_mejor = actual
                value_mejor = value
            
        self.tour = state_mejor
        self.value = value_mejor
        end = time()
        self.time = end-start
        return state_mejor

