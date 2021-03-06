#!/usr/bin/python
import csv
import time
def make_link(G, node1, node2):
	if node1 not in G:
		G[node1] = {}
	(G[node1])[node2] = 1
	if node2 not in G:
		G[node2] = {}
	(G[node2])[node1] = 1
	return G

def read_graph(filename):
	# reads an undirected graph in CSV format. Each line is an edge
	tsv = csv.reader(open(filename), delimiter='\t')
	G = {}
	for (node1, node2) in tsv:
		make_link(G, node1, node2)
	return G

# read the marvel comics graph
marvelG = read_graph("uniq_edges.tsv")

def path(G,v1,v2):
	distance_from_start = {}
	# path_from_start = {}
	open_list = [v1]
	distance_from_start[v1] = [v1]
	# path_from_start[v1] = [v1]
	while len(open_list) > 0:
		current = open_list[0]
		del open_list[0]
		for neighbor in G[current].keys():
			if neighbor not in distance_from_start:
				distance_from_start[neighbor] = distance_from_start[current] + [neighbor]
				if neighbor == v2:
					return distance_from_start[v2]
				open_list.append(neighbor)
	return False

from_node = 'A'
to_node = 'ZZZAX'
print path(marvelG, from_node, to_node)