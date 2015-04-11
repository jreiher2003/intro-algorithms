import random
###
###
#
# List of distinct two-digit values.
# Where will 84 be located in the sorted version
#
L = [31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36]

def rank(L, v):
	pos = 0
	for val in L:
		if val < v:
			pos += 1
	return pos

print rank(L, 84)

def partition(L, v):
	smaller = []
	bigger = []
	for val in L:
		if val < v: 
			smaller.append(val)
		if val > v:
			bigger.append(val)
	return smaller + [v] + bigger

print partition(L, 66)



def top_k(L,k):
	v = L[random.randrange(len(L))]
	(left,middle,right) = partition(L,v)
	if len(left) == k: return left
	if len(left)+1 == k: return left+[v]
	if len(left) > k: return top_k(left,k)
	return left+[v]+top_k(right,k-len(left)-1)

print top_k(L,5)