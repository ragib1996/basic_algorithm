adj = [[] for  i in range(0, 1000)]


def addEdge(u, v):
	adj[u].append(v)


def sort(i, adj,  visited, s):
	
    visited[i] = True

    for j in adj[i]:
	    if visited[j] == False:
		    sort(j, adj, visited, s)
	
    s.append(i)



def f(adj, v):
    
	position = {}
	s = []
	visited = [False] * v

	for i in range(0, v):
		if visited[i] == False:
			sort(i, adj,  visited , s )


	topological_sort = []
	while len(s) > 0:
		topological_sort.append(s[-1])
		position[s[-1] ] = len(topological_sort)
		s.pop()
	
	for i in range (0 ,len(adj) ):
		for j in adj[i]:
			first = position[i]
			second = position[j]
			if first < second:
				return True
			
	return False

if __name__ == "__main__":
	
	n = 4
	m = 5
	v = 6
    
	
	# Insert edges
	"""
	addEdge(0, 1)
	addEdge(0, 2)
	addEdge(1, 3)
	addEdge(4, 1)
	addEdge(4, 5)
	addEdge(5,3)
	addEdge(3,4)
    """

	addEdge(0, 1)
	addEdge(0, 2)
	addEdge(1, 2)
	addEdge(2, 0)
	addEdge(2, 3)
	#addEdge(5,3)
	#addEdge(3,4)
	#print(adj[:v])
	
	ans = f(adj, v)
	print(ans)
	