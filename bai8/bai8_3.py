
import turtle
colors = ["red", "blue", "green"]
painter = turtle.Turtle()
painter.pensize(3)
for i in range(12):
    color = colors[i % len(colors)]
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0, 0)