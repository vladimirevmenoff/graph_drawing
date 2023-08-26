def spring(g):
	from random import uniform

	n = len(g)
	inf = +1000000

	dp = [[inf for i in range(n)] for j in range(n)]

	for v in range(n):

		dp[v][v] = 0
		for u in g[v]:
			dp[v][u] = 1
			dp[u][v] = 1 
	        
	#Floyd-Warshall
	D = 0
	K = 10 
	for i in range(n):
		for j in range(n):
			for k in range(n):
				dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
			
			D = max(D, dp[i][j])		
	 
	L = n / D

	k = [[0 for i in range(n)] for j in range(n)]
	l = [[0 for i in range(n)] for j in range(n)]

	for i in range(n):
		for j in range(n):
			if i == j:
				continue
			k[i][j] = K / (dp[i][j] ** 2)
			l[i][j] = L * dp[i][j]
	print(L)

	coords = [[uniform(0, n), uniform(0, n)] for i in range(n)]

	def en():
		E = 0
		for i in range(n):
			for j in range(i + 1, n):
				E += 0.5 * k[i][j] * ((coords[i][0] - coords[j][0]) ** 2 +
						      (coords[i][1] - coords[j][1]) ** 2 + l[i][j] ** 2 -
						       2 * l[i][j] * (((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2) ** 0.5))

		return E

	def grad(m):
		eps = 0.0001
		
		E = en()
		coords[m][0] += eps
		E_x = en()
		coords[m][0] -= eps
		coords[m][1] += eps
		E_y = en()
		coords[m][1] -= eps

		return ((E_x - E) / eps, (E_y - E) / eps)

	def grad_step(max_iters = 300, learning_rate = 0.05, momentum = 0.8):
		
		iters = 0
		last_step = [[0, 0] for i in range(n)]
		gr = [[10, 10] for i in range(n)]

		while(sum([(gr[m][0] ** 2 + gr[m][1] ** 2) ** 0.5 for m in range(n)]) > 0.05 and
				 max_iters > iters):
			gr = [grad(i) for i in range(n)]
		
			for m in range(n):	
				coords[m][0] += -learning_rate * gr[m][0] + momentum * last_step[m][0]
				coords[m][1] += -learning_rate * gr[m][1] + momentum * last_step[m][1]
			
				last_step[m][0] = -learning_rate * gr[m][0] + momentum * last_step[m][0]
				last_step[m][1] = -learning_rate * gr[m][1] + momentum * last_step[m][1]

			iters += 1

	grad_step()

	return coords