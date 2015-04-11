#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the absolute value of the difference
# between each element in L and x: SUM_{i=0}^{n-1} |L[i] - x|
# 
# Your code should run in Theta(n) time
#
import random
import numpy

L = random.sample(range(10), 10)
# L = [1,4,2,7,5,3,9,6]
print L



def minimize_absolute(L):
    x = 0
    # your code here
    return numpy.median(numpy.array(L))

print minimize_absolute(L)

def minimize_square(L):
	sq = []
	for nums in L:
		sq.append(nums**2)
	return dir(sq)
		
def sum_of_squares(n):
    return sum([i**2 for i in range(1, n+1)])

print minimize_square(L)



