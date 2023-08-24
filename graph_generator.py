def generate_graph(n, m):
	from random import randint
	
 	
	weights = []	
	for i in range(n):
		for j in range(i + 1, n):
			weights.append([i, j, randint(0, 100000)])	

	weights.sort(key=lambda x : x[2])

	
	parent = [i for i in range(n)]
	g = [[] for i in range(n)]

	def find_parent(v):
		if parent[v] == v:
			return v

		parent[v] = find_parent(parent[v])
		return parent[v]

	def union(u, v):
		u = find_parent(u)
		v = find_parent(v)

		if u != v:
			parent[u] = v

	def add_edge(u, v):
		g[u].append(v)
		g[v].append(u)

	for i in range(len(weights)):
		edge = weights[i]
		u, v = edge[0], edge[1]
		
		if find_parent(u) != find_parent(v):
			union(u, v)
			weights[i][2] = -1
			add_edge(u, v)


	
	to_add = m - n + 1
	for edge in weights:
		if edge[2] != -1 and to_add > 0:
			add_edge(edge[0], edge[1])
			to_add -= 1

	return g

