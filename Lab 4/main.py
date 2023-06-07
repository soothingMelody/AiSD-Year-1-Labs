import random

class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

def generate(n, nas):
    adjList = [[] for _ in range(n + 1)]
    edges = []
    vertices = list(range(1, n + 1))
    random.shuffle(vertices)

    for i in range(n - 1):
        edges.append(Edge(vertices[i], vertices[i + 1]))
    edges.append(Edge(vertices[n - 1], vertices[0]))

    while len(edges) < nas * n * (n - 1) / 2:
        u = random.randint(1, n)
        v = random.randint(1, n)
        w = random.randint(1, n)

        if u != v and v != w and u != w:
            valid = True
            for edge in edges:
                if (edge.u == u and edge.v == v) or (edge.u == v and edge.v == w) or (edge.u == w and edge.v == u) \
                        or (edge.u == v and edge.v == u) or (edge.u == w and edge.v == v) or (edge.u == u and edge.v == w):
                    valid = False
                    break

            if valid:
                edges.append(Edge(u, v))
                edges.append(Edge(v, w))
                edges.append(Edge(w, u))

    for edge in edges:
        adjList[edge.u].append(edge.v)

    return adjList

if __name__ == '__main__':
    n = 10
    nas = 0.8
    adjList = generate(n, nas)

    with open("graf08.txt", "w") as file:
        ile = sum(len(adjList[u]) for u in range(1, n + 1))
        file.write(f"{n} {ile}\n")
        for u in range(1, n + 1):
            for v in adjList[u]:
                file.write(f"{u} {v}\n")

    ile = sum(len(adjList[u]) for u in range(1, n + 1))
    print(f"{n} {ile}")
    for u in range(1, n + 1):
        for v in adjList[u]:
            print(f"{u} {v}")
