from turtle import *

def draw_star(x,y,length):
    left(36)
    penup()
    goto(x,y)
    pendown()
    for i in range(5):
        forward(length)
        left(144)

# draw_star(120,100,150)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()

#random.randint() is to use randint function from random library
