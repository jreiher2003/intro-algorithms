import math

def make_a_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def clique(n):
    # Return the number of edges
    # Try to use a mathematical formula...
    G = {}
    # Add in the edges
    for i in range(n):
        for j in range(n-1):
            make_a_link(G, i, (i+1+j)%n)
    # How many edges?
    nEdges = sum([len(G[node]) for node in G.keys()])/2
    # nEdges = n * (n-1) / 2
    return nEdges

print clique(10)


def clique(n):
    # Return the number of edges
    # Try to use a mathematical formula...
    return n * (n-1) /2


print clique(10)