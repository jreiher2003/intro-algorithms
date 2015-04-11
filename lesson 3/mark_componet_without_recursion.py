def mark_component(G, node, marked):
	open_list = [node]
	total_marked = 1
	marked[node] = True
	while len(open_list) > 0:
		node = open_list.pop()
		for neighbor in G[node]:
			if neighbor not in marked:
				open_list.append(neighbor)
				marked[neighbor] = True
				total_marked += 1
	return total_marked