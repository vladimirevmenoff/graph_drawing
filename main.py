from graphics import *
from springs import spring

def main():
	win = GraphWin("My Circle", 800, 800)

	g = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2, 5], [4]]
	coords = spring(g)

	for i in range(len(coords)):
		coords[i][0] += 20
		coords[i][1] += 20 

		coords[i][0] *= 20
		coords[i][1] *= 20

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