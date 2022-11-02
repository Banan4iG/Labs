import sys

class Graph(object):
    def __init__(self, nodes, connections):
        self.nodes = nodes
        self.graph = self.init_graf(nodes, connections)
        
    def init_graf(self, nodes, connections):
        #Заполняет граф обратными данными. Если A->B, то должно и B->A"
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(connections)
        
        for from_node, to_nodes in graph.items():
            for to_node, value in to_nodes.items():
                if graph[to_node].get(from_node, False) == False:
                    graph[to_node][from_node] = value
                    
        return graph
        
    def get_to_nodes(self, node):
        #Возвращает соседей узла"
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        #Возвращает значение ребра между двумя узлами
        return self.graph[node1][node2]


    def dijkstra_algorithm(self, start_node, target_node):
        if start_node == target_node:
            print("Пункт отправления == Пункт назначения :)")
            return
        
        if not self.graph[target_node]:
            print("Отсутсвуют связи с Пунктом назначения :(")
            return

        if not self.graph[start_node]:
            print("Из Пункта отправления невозможно отправиться:(")
            return

        unvisited_nodes = list(self.nodes)

        if start_node not in unvisited_nodes or target_node not in unvisited_nodes:
            print("Пункт отправления и/или Пункт назначения не найден(ы) :(")
            return
        
        shortest_path = {}
    
        previous_nodes = {}
    
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
         
        shortest_path[start_node] = 0
        
        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node
                    
            neighbors = self.get_to_nodes(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + self.value(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_nodes[neighbor] = current_min_node
            unvisited_nodes.remove(current_min_node)
        
        path = []
        node = target_node
        
        while node != start_node:
            path.append(node)
            node = previous_nodes[node]
    
        path.append(start_node)
        
        print("Найден следующий маршрут: ")
        print(" -> ".join(reversed(path)))
        print("Расстоянием: " + str(shortest_path[target_node]))


nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
 
connections = {}
for node in nodes:
    connections[node] = {}
    
connections['A']['B'] = 1
connections['A']['C'] = 3
connections['B']['D'] = 5
connections['B']['G'] = 10
connections['C']['D'] = 8
connections['C']['F'] = 6
connections['D']['E'] = 3
connections['F']['G'] = 7

graph = Graph(nodes, connections)

graph.dijkstra_algorithm(start_node='H', target_node='B')
