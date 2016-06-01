def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = "|"
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = "|"
    return G


node1 = 2
node2 = 3
# print make_link(a_ring, node1, node2)

a_ring = {}
n = 5

# add in the edges
for i in range(n):
    make_link(a_ring, i, (i+1) % n)

# how many nodes?
print len(a_ring)

# how many edges?
print sum([len(a_ring[node]) for node in a_ring.keys()]) /2
print a_ring.keys()

print a_ring