import random
import time
from collections import defaultdict

def count_back_edges_adjacency_matrix(graph):
    n = len(graph)
    count = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and graph[j][i] == 1:
                count += 1

    return count

def count_back_edges_successor_list(graph):
    count = 0

    for node in graph:
        for neighbor in graph[node]:
            if node in graph[neighbor]:
                count += 1

    return count

def count_back_edges_edge_list(graph):
    count = 0

    for u, v in graph:
        if (v, u) in graph:
            count += 1

    return count

def topological_sort(graph):
    visited = set()
    start_time = {}
    end_time = {}
    timestamp = 0
    is_acyclic = True

    def dfs(node):
        nonlocal timestamp, is_acyclic
        visited.add(node)
        start_time[node] = timestamp
        timestamp += 1

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
            elif neighbor in start_time and neighbor not in end_time:
                is_acyclic = False

        end_time[node] = timestamp
        timestamp += 1

    graph = dict(graph)

    for node in graph:
        if node not in visited:
            dfs(node)

    return start_time, end_time, is_acyclic



# def generate_random_graph(n, density):
#     graph = defaultdict(list)
#     max_edges = (n * (n - 1)) // 2  # maksymalna liczba krawędzi w pełnym grafie
#
#     num_edges = int(density * max_edges)
#     edge_count = 0
#
#     while edge_count < num_edges:
#         node1 = random.randint(1, n)
#         node2 = random.randint(1, n)
#
#         if node2 not in graph[node1] and node1 != node2:
#             graph[node1].append(node2)
#             edge_count += 1
#
#     return graph

def generate_random_graph(n, density):
    graph = defaultdict(list)
    max_edges = (n * (n - 1)) // 2  # maximum number of edges in a complete graph

    num_edges = int(density * max_edges)
    edge_count = 0

    def dfs(node, visited):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, visited):
                    return True
            else:
                return True
        visited[node] = False
        return False

    # Initialize the visited dictionary with all nodes
    visited = {node: False for node in range(1, n+1)}

    while edge_count < num_edges:
        node1 = random.randint(1, n)
        node2 = random.randint(1, n)

        # Check if adding the edge creates a cycle
        graph[node1].append(node2)
        if dfs(node1, visited):
            graph[node1].remove(node2)  # Remove the edge if it creates a cycle
        else:
            edge_count += 1

    return graph

# Przykład użycia
n_values = [300, 350, 400, 450, 500, 600, 700, 800, 900, 1000]
density = [0.2, 0.4]

for n in n_values:
    for d in density:
        graph = generate_random_graph(n, d)
        start_time2 = time.time()
        start_time, end_time, is_acyclic = topological_sort(graph)
        end_time2 = time.time()
        sorting_time = end_time2 - start_time2
        #temporary_count_var = count_back_edges_edge_list
        print("n =", n, " d =", d)
        #print("count =", temporary_count_var)
        #print("Sorting Time:", sorting_time)
        #print("Start time:", start_time)
        #print("End time:", end_time)
        print("Is acyclic?", is_acyclic)