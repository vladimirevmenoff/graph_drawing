from graphics import *

def main():
	win = GraphWin("My Circle", 100, 100)
	c = Circle(Point(50,50), 10)
	c.draw(win)
	win.getMouse() # Pause to view result
	win.close()

if __name__ == '__main__':
	main()