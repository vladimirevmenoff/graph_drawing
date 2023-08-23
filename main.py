from graphics import *
from springs import spring

WIDTH = 800
HEIGHT = 800

def main():


	win = GraphWin("My Graph", WIDTH, HEIGHT)

	g = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2, 5], [4]]
	coords = spring(g)

	# adjust image
	u = max([_[1] for _ in coords])
	d = min([_[1] for _ in coords])

	l = max([_[0] for _ in coords])
	r = min([_[0] for _ in coords])

	for i in range(len(coords)):
		coords[i][0] -= l
		coords[i][1] -= d

		coords[i][0] /= (r - l)
		coords[i][1] /= (u - d)

		coords[i][0] *= (WIDTH - 10)
		coords[i][1] *= (HEIGHT - 10)

		coords[i][0] += 5
		coords[i][1] += 5


	for i in coords:
		c = Circle(Point(i[0], i[1]), 1)
		c.draw(win)

	for u in range(len(g)):
		for v in g[u]:
			line = Line(Point(coords[u][0], coords[u][1]), Point(coords[v][0], coords[v][1]))
			line.draw(win)


	win.getMouse() # Pause to view result
	win.close()

if __name__ == '__main__':
	main()