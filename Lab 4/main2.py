import time
from collections import defaultdict, deque

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def euler_cycle(self):
        start_vertex = 1  # Choose any vertex as the starting point
        cycle = []
        stack = [start_vertex]

        while stack:
            current_vertex = stack[-1]

            if self.adj_list[current_vertex]:
                next_vertex = self.adj_list[current_vertex].pop()
                self.adj_list[next_vertex].remove(current_vertex)
                stack.append(next_vertex)
            else:
                cycle.append(stack.pop())

        return cycle[::-1]  # Reverse the cycle to get the correct order

    def hamiltonian_cycle(self):
        cycle = []
        stack = deque()
        visited = [False] * (self.num_vertices + 1)
        stack.append(1)
        visited[1] = True

        while stack:
            current_vertex = stack[-1]
            cycle.append(current_vertex)

            if len(cycle) == self.num_vertices:
                if 1 in self.adj_list[current_vertex]:
                    cycle.append(1)
                    return cycle

            found_next = False
            for neighbor in self.adj_list[current_vertex]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True
                    found_next = True
                    break

            if not found_next:
                last_visited = stack.pop()
                visited[last_visited] = False
                cycle.pop()

        return cycle

    def all_hamiltonian_cycles(self):
        cycles = []

        def backtrack(current_vertex, start_vertex, path, visited):
            nonlocal cycles

            # If all vertices are visited and there is an edge back to the starting vertex, check if it forms a Hamiltonian cycle
            if len(path) == self.num_vertices and start_vertex in self.adj_list[current_vertex]:
                cycle = path + [start_vertex]

                # Check if the cycle is a Hamiltonian cycle by verifying if it visits each vertex exactly once
                if set(cycle) == set(range(1, self.num_vertices + 1)):
                    cycles.append(cycle)

                return

            # Try all neighbors of the current vertex
            for neighbor in self.adj_list[current_vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    path.append(neighbor)
                    backtrack(neighbor, start_vertex, path, visited)
                    path.pop()
                    visited[neighbor] = False

        # Start the backtracking from each vertex
        for vertex in range(1, self.num_vertices + 1):
            path = [vertex]
            visited = [False] * (self.num_vertices + 1)
            visited[vertex] = True
            backtrack(vertex, vertex, path, visited)

        return cycles


def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        num_vertices, _ = map(int, file.readline().split())
        graph = Graph(num_vertices)

        for line in file:
            u, v = map(int, line.split())
            graph.add_edge(u, v)

    return graph


# Example usage
filename = 'graf08.txt'
#graph = read_graph_from_file(filename)
#st1 = time.time()
#euler_cycle = graph.euler_cycle()
#print("Euler Cycle:", "Time:", time.time()-st1)
graph = read_graph_from_file(filename)
st2 = time.time()
hamiltonian_cycle = graph.hamiltonian_cycle()
print("Hamiltonian Cycle:", "Time:", time.time()-st2)
#graph = read_graph_from_file(filename)
#st3 = time.time()
#all_ham_cycles = graph.all_hamiltonian_cycles()
#print("All Hamiltonian Cycles:", len(all_ham_cycles), "Time:", time.time() - st3)
