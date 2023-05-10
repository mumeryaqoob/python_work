#Muhammad Umer 18B-030-CE
import matplotlib.pyplot as plt
import numpy as np
xwmin = int(input("Enter world coordinate x (xwmin) : "))
ywmin = int(input("Enter world coordinate y (ywmin) : "))
xwmax = int(input("Enter world coordinate x (xwmax) : "))
ywmax = int(input("Enter world coordinate x (ywmax) : "))
px1 = int(input("Enter coordinate  x1 (px1) : "))
py1 = int(input("Enter coordinate y1 (py1) : "))
px2 = int(input("Enter coordinate x2 (px2) : "))
py2 = int(input("Enter coordinate y2 (py2) : "))
plt.subplots()
geometry = np.array([[xwmin,ywmin],[xwmin,ywmax],[xwmax,ywmax],[xwmax,ywmin],[xwmin,ywmin]])
line = np.array([[px1,py1],[px2,py2]])
plt.plot(geometry[:,0],geometry[:,1])
plt.plot(line[:,0],line[:,1])
A = 1  #0001
B = 2  #0010
C = 4  #0100
D = 8  #1000
E = 0  #0000
F = 5  #0101
G = 6  #0110
H = 9  #1001
I = 10 #1010
def assign_code(A,B,C,D,E,F,G,H,I,px1,px2,py1,py2,xwmin,ywmin,xwmax,ywmax):
    code1 = 0 #INITIALLY
    code2 = 0 #INITIALLY
    if (px1<xwmin and ywmin<py1<ywmax):
        code1 = A
    elif (px1 > xwmax and ywmin < py1 < ywmax):
        code1 = B
    elif (py1 < ywmin and xwmin < px1 < xwmax):
        code1 = C
    elif (py1 > ywmax and xwmin < px1 < xwmax):
        code1 = D
    elif (xwmin < px1 < xwmax and ywmin < py1 < ywmax):
        code1 = E
    elif (px1 < xwmin and py1 < ywmin):
        code1 = F
    elif (px1 > xwmax and py1 < ywmin):
        code1 = G
    elif (px1 < xwmin and py1 > ywmax):
        code1 = H
    elif (px1 > xwmax and py1 > ywmax):
        code1 = I
    else:
        code = E
    if (px2 < xwmin and ywmin < py2 < ywmax):
        code2 = A
    elif (px2 > xwmax and ywmin < py2 < ywmax):
        code2 = B
    elif (py2 < ywmin and xwmin < px2 < xwmax):
        code2 = C
    elif (py2 > ywmax and xwmin < px2 < xwmax):
        code2 = D
    elif (xwmin < px2 < xwmax and ywmin < py2 < ywmax):
        code2 = E
    elif (px2 < xwmin and py2 < ywmin):
        code2 = F
    elif (px2 > xwmax and py2 < ywmin):
        code2 = G
    elif (px2 < xwmin and py2 > ywmax):
        code2 = H
    elif (px2 > xwmax and py2 > ywmax):
        code2 = I
    else:
        code = E
    print("The point p1 of line is assigned with code1", code1)
    print("The point p2 of line is assigned with code2", code2)
    return code1, code2
def check_visibility(code1, code2):
    if (code1 | code2) == 0:
        print("Line is inside the window")
        plt.text(px1, py1, 'P1')
        plt.text(px2, py2, 'P2')
        plt.title("The Line is inside the window")
        plt.show()
    elif (code1 & code2) > 0 and (code1|code2) > 0 :
        print("Line is completely outside")
        plt.text(px1,py1,'P1')
        plt.text(px2,py2,'P2')
        plt.title("The Line is completely outside")
        plt.show()
    elif (code1&code2) == 0 and (code1|code2) > 0 :
        print("Line is partially visible")
        plt.text(px1,py1,'P1')
        plt.text(px2,py2,'P2')
        plt.title("The Line is partially visible")
        plt.show()
code1,code2 = assign_code(A,B,C,D,E,F,G,H,I,px1,px2,py1,py2,xwmin,ywmin,xwmax,ywmax)
check_visibility(code1,code2)
