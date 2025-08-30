import networkx as nx
import matplotlib.pyplot as plt
import random
from itertools import permutations

random.seed(42)  # reprodutibilidade
n = 8  # número de vértices

# --- Verifica condição de Ore ---
def satisfies_ore(G):
    n = G.number_of_nodes()
    nodes = list(G.nodes())
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            u, v = nodes[i], nodes[j]
            if not G.has_edge(u, v):
                if G.degree(u) + G.degree(v) < n:
                    return False
    return True

# --- Busca exaustiva por ciclo Hamiltoniano ---
def find_hamiltonian_cycle(G):
    n = G.number_of_nodes()
    nodes = list(G.nodes())
    if n == 0:
        return None
    start = nodes[0]
    for perm in permutations(nodes[1:]):
        cycle = (start,) + perm + (start,)
        ok = True
        for a, b in zip(cycle[:-1], cycle[1:]):
            if not G.has_edge(a, b):
                ok = False
                break
        if ok:
            return cycle[:-1]  # retorna sequência de vértices
    return None

# --- Gera um grafo aleatório que satisfaça Ore ---
attempt = 0
while True:
    attempt += 1
    G = nx.Graph()
    G.add_nodes_from(range(n))
    p = 0.75  # probabilidade de aresta
    for u in range(n):
        for v in range(u+1, n):
            if random.random() < p:
                G.add_edge(u, v)
    if G.number_of_edges() == n*(n-1)//2:
        continue  # se for completo, não é interessante
    if satisfies_ore(G):
        break

print(f"Tentativas até encontrar grafo: {attempt}")
print(f"Vértices: {n}, Arestas: {G.number_of_edges()}")
print("Grau dos vértices:", dict(G.degree()))

ore_ok = satisfies_ore(G)
ham_cycle = find_hamiltonian_cycle(G)

print(f"Cond. de Ore satisfeita? {ore_ok}")
print(f"Ciclo Hamiltoniano encontrado? {'Sim' if ham_cycle else 'Não'}")
if ham_cycle:
    print("Ciclo Hamiltoniano:", ham_cycle)

# --- Plotagem ---
pos = nx.spring_layout(G, seed=1)
plt.figure(figsize=(8,6))
nx.draw(G, pos, with_labels=True, node_size=500, font_size=10)

if ham_cycle:
    cycle_edges = [(ham_cycle[i], ham_cycle[(i+1)%len(ham_cycle)]) for i in range(len(ham_cycle))]
    nx.draw_networkx_edges(G, pos, edgelist=cycle_edges, width=3)
    plt.title("Grafo que satisfaz a condição de Ore — ciclo Hamiltoniano destacado")
else:
    plt.title("Grafo que satisfaz a condição de Ore — nenhum ciclo Hamiltoniano encontrado")

plt.axis('off')
plt.show()
