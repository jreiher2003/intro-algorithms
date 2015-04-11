###
#
#
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

    # your code here
    print 'up_heapify i=', i , 'len(L)=', len(L)   
    if i == 0:
        return
    
    if len(L) == (i+1):
        if L[i] < L[parent(i)]:
            (L[i], L[parent(i)]) = (L[parent(i)], L[i])
        up_heapify(L, parent(i))
        return
    
    # two child
    if min(L[i], L[i+1]) < L[parent(i)]:
        if L[i] > L[i+1]:
            (L[i+1], L[parent(i)]) = (L[parent(i)], L[i+1])
        else:
            (L[i], L[parent(i)]) = (L[parent(i)], L[i])
        
    up_heapify(L, parent(i))
    return
