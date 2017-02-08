import turtle
import time
import random

def draw_rectangle(length, height):
    turtle.up()
    x = -150
    y = 150
    C = height*(7/13)
    D = length*(2/5)
    L = stripe_width = float(round(height/13,1))

    ## Draw rectangle first.
    turtle.color(0,0,0)
    turtle.begin_fill()
    turtle.setpos(x,y)
    turtle.down()
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(height)
    turtle.end_fill()

    ## Then draw the stripes.
    x1 = -150
    y1 = 150-L
    for z in range(13):
        if z%2 == 0:
            #r = s = t = 0
            r = 1
            s = t = 0
        else:
            r = s = t = 1
        turtle.up()
        turtle.speed(100)
        turtle.setpos(x1,y1)
        turtle.setheading(90)
        turtle.down()
        turtle.color(r,s,t)
        turtle.begin_fill()
        turtle.forward(L)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(L)
        turtle.right(90)
        turtle.forward(length)
        turtle.end_fill()
        y1 -= L

    ## Finally draw the stars rectangle overlapping the stripes, next is stars.
    x2 = -150+D
    y2 = 150.5-C
    turtle.up()
    turtle.setpos(x2,y2)
    turtle.down()
    turtle.color(0,0,1)
    turtle.begin_fill()
    turtle.forward(D)
    turtle.right(90)
    turtle.forward(C)
    turtle.right(90)
    turtle.forward(D)
    turtle.right(90)
    turtle.forward(C)
    turtle.end_fill()
    turtle.up()

    turtle.bye
    draw_star(-length, height)

def draw_star(l, h):
    for z in range(50):
        if z < 7:
            row = 140
            draw_starrows(row)
        if z < 14:
            row = row - 20
            draw_starrows(row)
        if z < 21:
            row = row - 20
            draw_starrows(row)
        if z < 28:
            row = row - 20
            draw_starrows(row)
        if z < 35:
            row = row - 20
            draw_starrows(row)
            ## This gets the turtle pen out of the way at the very end.
            turtle.up()
            turtle.setpos(-180,100)
        break

def draw_starrows(row):
    x = -160
    y = 150
    for z in range(10):
        x += 15
        turtle.up()
        turtle.color(1,1,1)
        turtle.speed(100)
        turtle.setpos(x,row)
        turtle.begin_fill()
        turtle.down()
        turtle.forward(6.154)
        turtle.left(144)
        turtle.forward(6.154)
        turtle.left(144)
        turtle.forward(6.154)
        turtle.left(144)
        turtle.forward(6.154)
        turtle.left(144)
        turtle.forward(6.154)
        turtle.left(144)
        turtle.end_fill()
    turtle.bye

##def get_color():
##    r = g = b = 0
##    color = r = g = b
##    return color

def draw_flag():
    A = 200
    height = int(A)
    ##    length = height*1.9
    ##    C = height*(7/13)
    ##    D = length*(2/5)
    ##    E = F = union_height/10
    ##    G = H = union_length/12
    ##    stripe_width = height/13
    ##    diameter_star = stripe_width*(4/5)
    draw_rectangle(height*1.9, height)
    turtle.exitonclick()

draw_flag()