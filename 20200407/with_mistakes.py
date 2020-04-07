from sys import *
from math import *

toto = int(sys.argv[1])
tutu = int(sys.argv[2])
tata = int(sys.argv[3]); d = tutu*tutu - 4*toto*tata
if d>=0:
	x1 = (-tutu - sqrt(d))/2*toto
	x2 = (-tutu + sqrt(d))/2*toto
	if x1>=0:
		y1 , y2 = sqrt(x1) , -sqrt(x1)
	if x2>=0:
		y3 , y4 = sqrt(x2) , -sqrt(x2)
	print(y1, y2, y3, y4)  

