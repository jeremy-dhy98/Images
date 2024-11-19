import random
from graphics import *
import time

win = GraphWin("RandomCircles", 300, 300)


# Create 20 circles of diff radius
def main():
    for circle in range(20):
        x = random.randrange(5, 200)
        y = random.randrange(5, 200)
        p = Point(x, y)
        radius = random.randrange(3, 40)
        # Colour for the circles
        r = random.randrange(150)
        g = random.randrange(150)
        b = random.randrange(150)
        my_color = color_rgb(r, g, b)
        circle = Circle(p, radius)
        circle.setFill(my_color)
        circle.move(50, 70)
        circle.draw(win)
        time.sleep(1.5)
    win.getMouse() # Keep the win on
    win.close() 


if __name__ == "__main__":
    main()
