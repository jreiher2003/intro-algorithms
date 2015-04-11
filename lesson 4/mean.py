# list of node centrality values from example graph
# running time is big theta(n)
L = [2,3,2,3,2,4]

def mean(L):
	total = 0
	for i in range(len(L)):
		total += L[i]
	return (0.0+total)/len(L)
print mean(L)

# or still big theta(n)
print (0.0+sum(L))/len(L)
# linear time operation
def max(L):
	max_so_far = L[0]
	for i in range(1,len(L)):
		if L[i] > max_so_far: max_so_far = L[i]
	return max_so_far

print max(L)