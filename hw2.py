from turtle import *
wn = Screen()
wn.setup(width=400, height=400)
red = Turtle()
pensize(2)
color('red', 'yellow')
def curve():
    for i in range(200):
        red.right(1)
        red.forward(1)
def heart(a):
    red.fillcolor(a)
    red.begin_fill()
    red.left(140)
    red.forward(113)
    curve()
    red.left(120)
    curve()
    red.forward(112)
    red.end_fill()
speed(0)
for colours in ['red','orange','blue','yellow','green','purple']:
    speed(0)
    heart(colours)
red.ht()
done()
