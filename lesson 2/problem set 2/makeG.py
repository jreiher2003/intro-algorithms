#Recurrence Relation

def makeG(N):
	if n == 1:
		return <a single node>
	g1 = makeG(n/2)
	g2 = makeG(n/2)
	for i in range(log(n)):
		i1 = <random node from g1 without replacement>
		i2 = <random node from g2 without replacement>
		make_link(G, il, i2)
	return G

	