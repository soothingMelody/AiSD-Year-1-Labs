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

def generate_random_graph_adjacency_matrix(n, density):
    graph = [[0] * n for _ in range(n)]
    num_edges = int(density * n * (n - 1) / 2)

    edges = random.sample(range(n * n), num_edges)
    for edge in edges:
        u = edge // n
        v = edge % n
        graph[u][v] = 1

    return graph

def generate_random_graph_successor_list(n, density):
    graph = defaultdict(list)
    max_edges = (n * (n - 1)) // 2  # maksymalna liczba krawędzi w pełnym grafie

    num_edges = int(density * max_edges)
    edge_count = 0

    while edge_count < num_edges:
        node1 = random.randint(1, n)
        node2 = random.randint(1, n)

        if node2 not in graph[node1] and node1 != node2:
            graph[node1].append(node2)
            edge_count += 1

    return graph

def generate_random_graph_edge_list(n, density):
    graph = []
    max_edges = (n * (n - 1)) // 2  # maksymalna liczba krawędzi w pełnym grafie

    num_edges = int(density * max_edges)
    edge_count = 0

    while edge_count < num_edges:
        u = random.randint(1, n)
        v = random.randint(1, n)
        edge = (u, v)

        if edge not in graph and u != v:
            graph.append(edge)
            edge_count += 1

    return graph

# Przykład użycia
n_values = [300, 400, 500, 600, 700]
density_values = [0.2, 0.4]

for density in density_values:
    print("Density:", density)
    print("-------------------------------")
    print("n\tAdjacency Matrix\tSuccessor List\t\tEdge List")
    print("----------------------------------------------------------")
    for n in n_values:
        graph_adj_matrix = generate_random_graph_adjacency_matrix(n, density)
        graph_succ_list = generate_random_graph_successor_list(n, density)
        graph_edge_list = generate_random_graph_edge_list(n, density)

        start_time_adj_matrix = time.time()
        back_edge_count_adj_matrix = count_back_edges_adjacency_matrix(graph_adj_matrix)
        end_time_adj_matrix = time.time()
        time_adj_matrix = end_time_adj_matrix - start_time_adj_matrix

        start_time_succ_list = time.time()
        back_edge_count_succ_list = count_back_edges_successor_list(graph_succ_list)
        end_time_succ_list = time.time()
        time_succ_list = end_time_succ_list - start_time_succ_list

        start_time_edge_list = time.time()
        back_edge_count_edge_list = count_back_edges_edge_list(graph_edge_list)
        end_time_edge_list = time.time()
        time_edge_list = end_time_edge_list - start_time_edge_list

        print(f"{n}\t{time_adj_matrix}\t\t\t{time_succ_list}\t\t\t{time_edge_list}")

    print("\n")
