from random import *
from turtle import *

def stop(x, y):
	global f
	f = False

f = True

shape("turtle")
pensize(3)

getscreen().onclick(stop)
while f:
	color(random(),random(), random())
	radius = randrange(-60,60)
	circle(radius, randrange(200))
	while not(abs(xcor()) < window_width()/2  and abs(ycor()) < window_height()/2):
		circle(radius, randrange(23))