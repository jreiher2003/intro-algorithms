

flist = []
names = open('names.txt', 'r')
for line in names:
	line = line.strip()
	line = line.split(',')
	if line[1] == 'F':
		flist.append((int(line[2]), line[0]))

flist.sort()
flist.reverse()
print flist[0:3]


	
