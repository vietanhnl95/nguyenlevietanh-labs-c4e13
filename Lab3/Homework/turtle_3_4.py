from turtle import *

def draw_square(length,line_color):
    speed(-1)
    color(line_color)
    for n in range(4):
        forward(length)
        left(90)

# draw_square(150,'blue')

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()
