import turtle
import math
from turtle import *


def arc(r, angle):
    """
    Draws a circle where r is the radius of that circle and angle is the
    amount of the circle you want to draw where 360 is one full circle
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    for i in range(n):
        forward(step_length)
        left(step_angle)


def flower(petals, petal_width):
    next_angle = 0
    for i in range(petals):
        # calculates the radius of the arc's circle needed to keep a constant size flower
        arc((200/math.sin(math.radians(petal_width/2))) * 0.5, petal_width)
        left(180 - petal_width)
        arc((200/math.sin(math.radians(petal_width/2))) * 0.5, petal_width)
        next_angle += 360/petals
        setheading(0)
        left(next_angle)


flower(12, 15)


done()
