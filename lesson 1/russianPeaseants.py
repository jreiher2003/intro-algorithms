# Russian Peasants Algorithm

def russian(a,b):
    x = a; y = b
    z = 0
    while x > 0: 
        if x % 2 == 1: 
            print x, z, y
            z = z + y
        y = y << 1
        x = x >> 1
    return z

print russian(63,12)
# print 27 >> 1
# print 17 << 1

#y
# print 7 << 1
# print 14 << 1
# print 28 << 1
# print 56 << 1
# print 112 << 1

# #x 19 9 3 1
# print 20 >> 1
# print 10 >> 1
# print 5 >> 1
# print 2 >> 1
# print 1 >> 1