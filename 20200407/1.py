""" Ввод с клавиатуры"""
import sys
import math
if __name__ == "__main__":
    A, B, C = (int(i) for i in sys.argv[1:4])
    D = B*B - 4*A*C
    if D >= 0:
        X1 = (-B - math.sqrt(D))/2*A
        X2 = (-B + math.sqrt(D))/2*A
        if X1 >= 0:
            Y1 = math.sqrt(X1)
            Y2 = -math.sqrt(X1)
        if X2 >= 0:
            Y3 = math.sqrt(X2)
            Y4 = -math.sqrt(X2)
        print(Y1, Y2, Y3, Y4)
    else:
        print("No roots")

