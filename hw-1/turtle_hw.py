from random import *
from turtle import *

border = 300

pensize(3)
penup()
goto(-border/2, -border/2)
pendown()

for _ in range(4):
	forward(border)
	left(90)

penup()
home()
pendown()

shape("turtle")
pensize(3)
while True:
	color(random(),random(), random())
	circle(randrange(-60,60),randrange(200))
