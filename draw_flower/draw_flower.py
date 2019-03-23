# This program draws a simple flower by using turtle!

import turtle

def draw_flower():
    
    #set up a window
    window = turtle.Screen()
    window.bgcolor("red")

    #set up a brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(15)

    #Drawing a flower
    for i in range(36):
        brad.right(10)
        for j in range(4):
            brad.forward(100)
            brad.right(90)
            j += 1
        i += 1

draw_flower()
