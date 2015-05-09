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
marvelG = read_graph("marvel_characters.tsv")
# make a character-to-character graph
# not that if an edge is added muliple times, the strength increases
time1 = time.time()
charG = {}
for char1 in characters:
	for book in marvelG[char1]:
		for char2 in marvelG[book]:
			if char1 > char2:
				make_link(charG, char1, char2)
time2 = time.time()
print "time to compute strenghts: ", time2-time1

# Get highest k strengths
time1 = time.time()
k = 10
heap = []
for char1 in characters:
	for char2 in charG[char1]:
		# avoid dups by only including pairs where the characters
		# number of the first is less that that of the second.
		if characters[char1] < characters[char2]:
			if len(heap) < k:
				insert_heap(heap, (charG[char1][char2],(char1,char2)))
			elif charG[char1][char2] > val(heap[0])