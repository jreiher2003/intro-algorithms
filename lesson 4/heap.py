#
#
#
#
# heap shortcuts
def left(i): 
	return i*2 + 1

def right(i):
	return i*2 + 2

def parent(i):
	return (i-1)/2

def root(i):
	return i == 0

def leaf(L, i):
	return right(i) >= len(L) and left(i) >= len(L)

def one_child(L,i): 
	return right(i) == len(L)

# call this routine if the heap rooted at i satisfies the heap property 
# *except* perhaps i to its children immediate children 
def down_heapify(L, i):
	# if i is a leaf, heap property holds
	if leaf(L,i):
		return
	# if i has on child...
	if one_child(L,i):
		# check heap property 
		if L[i] > L[left(i)]:
			# if it fails, swap, fixing i and its child (a leaf)
			(L[i], L[left(i)]) = (L[left(i)], L[i])
		return
	# if i has two children...
	# check heap property 
	if min(L[left(i)], L[right(i)]) >= L(i):
		return
	# if it fails, see which child is the smaller
	# and swap i's value into that child
	# afterwards, recurse into that child, which might violate
	if L[left(i)] < L[right(i)]:
		# swap into left child
		(L[i], L[left(i)]) = (L[left(i)], L[i])
	down_heapify(L, left(i))
	return
	(L[i], L[right(i)]) = (L[right(i)], L[i])
	down_heapify(L,right(i))
	return


def remove_min(L):
	top = L[0]
	bottom = L[len(L)-1]
	L.remove(top)
	L.insert(0,bottom)
	down_heapify(L,0)
	return L

def heap_sort(L):
	build_heap(L,0)
	while len(L) > 0:
	print L[0]
	remove_min(L)

def build_heap(L,i):
	if i == leaf: return
	down_heapify(L,i)
	return


# running time is theta(nlogn)
def insert_heap(L,v):
	L.append(v)
	up_heapify(L, len(L)-1)
	
heap = []
for v in vals:
	insert_heap(heap,v)