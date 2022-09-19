# LAB6- Coding and Implemetation
# Solve Travelling Salesman Problem solved using the Hill Climbing Algorithm
# Indrashis Paul
# 19MIM10046

import random
import networkx as nx
import matplotlib.pyplot as plt

class HillClimbing:
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.path = []
        self.visited = []
        self.current = start
        self.path.append(start)
        self.visited.append(start)
        self.distance = 0

    def get_next(self):
        """ Get the next node with the lowest cost """
        next = None
        for i in range(len(self.graph)):
            if self.graph[self.current][i] != 0 and i not in self.visited:
                if next is None:
                    next = i
                elif self.graph[self.current][i] < self.graph[self.current][next]:
                    next = i
        return next

    def get_distance(self):
        """ Get the total distance of the path """
        for i in range(len(self.path) - 1):
            self.distance += self.graph[self.path[i]][self.path[i + 1]]
        self.distance += self.graph[self.path[-1]][self.path[0]]

    def solve(self):
        """ Solve the TSP problem """
        while len(self.visited) < len(self.graph):
            next = self.get_next()
            if next is None:
                break
            self.path.append(next)
            self.visited.append(next)
            self.current = next
        self.get_distance()
        return self.path, self.distance


class TravellingSalesman:
    """ Generating a Travelling Salesman Problem and solving it with Hill Climbing Algorithm """
    def __init__(self, n):
        """ Initializing the problem with a random graph of size n """
        self.graph = self.problem_generator(n)
        self.min_path = []
        self.min_distance = 0
    
    def problem_generator(self, n):
        """ Generating a random graph of size n """
        graph = []
        for i in range(n):
            row = []
            for j in range(n):
                if i == j:
                    row.append(0)
                else:
                    row.append(random.randint(1, 100))
            graph.append(row)
        print("Graph:", graph)
        # plot the graph
        G = nx.DiGraph(name="Initial Graph")
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j] != 0:
                    G.add_edge(i, j, weight=graph[i][j])
        color_map = []
        for node in G:
            color_map.append('red')
        pos = nx.circular_layout(G)
        nx.draw(G, pos, with_labels=True, node_color=color_map)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
    
        return graph

    def solve(self):
        """ Solving the problem with Hill Climbing Algorithm """
        for i in range(len(self.graph)):
            hc = HillClimbing(self.graph, i)
            path, distance = hc.solve()
            if self.min_distance == 0 or distance < self.min_distance:
                self.min_distance = distance
                self.min_path = path
            print("Path: ", path, " Distance: ", distance)
        return self.min_path, self.min_distance

    def draw(self):
        """ Drawing the directed graph with the highlighted best path """
        G = nx.DiGraph(name="Best Path")
        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if self.graph[i][j] != 0:
                    G.add_edge(i, j, weight=self.graph[i][j])
        color_map = []
        for node in G:
            if node in self.min_path:
                color_map.append('lime')
            else:
                color_map.append('plum')
        pos = nx.circular_layout(G)
        nx.draw(G, pos, with_labels=True, node_color=color_map)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
        


if __name__ == "__main__":
    n = int(input("Enter the number of cities: "))
    tsp = TravellingSalesman(n)
    path, distance = tsp.solve()
    print("\nBest Path:", path, "Best Distance:", distance)
    tsp.draw()