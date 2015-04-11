def clique(n):
	print "in a clique..."
	for j in range(n):
		for i in range(j):
			print i, "is friends with", j

print clique(4)

def count(n):
	result = 2
    for i in range(n):
    	increment = i+1
    	result += increment
    return result

print count(24)
