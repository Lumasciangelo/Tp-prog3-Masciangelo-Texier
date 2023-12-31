from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node
import math

def distancia_linea_recta(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2

    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

def distancia_manhattan(punto1, punto2):
    distancia = 0
    for i in range(len(punto1)):
        distancia += abs(punto1[i] - punto2[i])

    return distancia

class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
         # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        frontier = PriorityQueueFrontier()
        frontier.add(node, distancia_manhattan(grid.start, grid.end))

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Add the node to the explored dictionary
        explored[node.state] = 0
        
        while True:
             #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(explored)
            
            node = frontier.pop()
            successors = grid.get_neighbours(node.state)

            if node.state == grid.end:
               return Solution(node, explored)
            
            for movimiento in successors:
                new_state = successors[movimiento]
                new_cost = node.cost + grid.get_cost(new_state) # NO CONFUNDIR LA PRIORIDAD CON EL COSTO EN SI 

                if (new_state not in explored) or (new_cost < explored[new_state]):
                    new_node = Node("", new_state, new_cost,
                                     parent=node, action=movimiento)
                    
                    explored[new_state] = new_cost

                    frontier.add(new_node, new_cost + distancia_manhattan(new_state, grid.end))

        return NoSolution(explored)
