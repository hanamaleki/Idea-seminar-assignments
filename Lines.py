import rhinoscriptsyntax as rs
import random
a = 20
x = random.randint(0,a)
y = random.randint(0,a)
z = random.randint(0,a)
p = (x,y,z)
p1 = (0,0,0)
p2 = (a,a,0)
p3 = (0,0,a)


for i in range(a):
    for j in range(a):
        point = (0,i,j)
        A = rs.AddPoint(point)
        rs.HideObject(A)
        B = rs.AddLine(point,p)
        rs.TrimCurve(B,(1,3),True)
        
