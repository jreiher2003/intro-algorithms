# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def is_tour(graph):
    nodes = {}
    for pair in graph:
        for item in pair:
            nodes.setdefault(item, 0)
            nodes[item] += 1

    for node in nodes:
        if nodes[node] % 2 != 0:
            return False
    return True

def valid_edge(edge, history):
    if edge in history or get_reversed(edge) in history:
        return False
    return True

def get_options(src, graph, history):
    options = []
    for i in range(len(graph)):
        if valid_edge(graph[i], history):
            if graph[i][0] == src or graph[i][1] == src:
                options.append(graph[i])
                options.append(get_reversed(graph[i]))
    return options

def get_reversed(edge):
    return (edge[1], edge[0])

def recursive_dfs(src, graph, history, path):
    path.append(src)

    if len(path) == len(graph) + 1:
        return path

    options = get_options(src, graph, history)
    for option in options:
        if option[1] != src:
            history.append(option)
            result = recursive_dfs(option[1], graph, history, path)
            if result:
                return result
            history.pop()
    path.pop()
    return None

def find_eulerian_tour(graph):
    if is_tour(graph):    
        return recursive_dfs(graph[0][0], graph, [], [])
    else:
        return None



