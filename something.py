import rhinoscriptsyntax as rs
import random
a = rs.AddPoint(0,0,0)
b = rs.AddPoint(0,0,50)
c = rs.AddPoint(0,50,50)
d = rs.AddPoint(0,50,0)
e = rs.AddPoint(50,50,50)
f = rs.AddPoint(50,50,0)
g = rs.AddPoint(50,0,0)
h = rs.AddPoint(50,0,50)
x1 = random.randint(0,50)
y1 = random.randint(0,50)
z1 = random.randint(0,50)
x2 = random.randint(0,50)
y2 = random.randint(0,50)
z2 = random.randint(0,50)
x3 = random.randint(0,50)
y3 = random.randint(0,50)
z3 = random.randint(0,50)
x4 = random.randint(0,50)
y4 = random.randint(0,50)
z4 = random.randint(0,50)
p1 = rs.AddPoint(x1,y1,z1)
p2 = rs.AddPoint(x2,y2,z2)
p3 = rs.AddPoint(x3,y3,z3)
p4 = rs.AddPoint(x4,y4,z4)
A = rs.AddInterpCurve([a,p1,b],3,0,None,None)
B = rs.AddInterpCurve([c,p2,d],3,0,None,None)
C = rs.AddInterpCurve([e,p3,f],3,0,None,None)
D = rs.AddInterpCurve([g,p4,h],3,0,None,None)
m = 20
A1 = rs.DivideCurve(A,m,True,True)
B1 = rs.DivideCurve(B,m,True,True)
C1 = rs.DivideCurve(C,m,True,True)
D1 = rs.DivideCurve(D,m,True,True)
rs.AddLoftSrf([A,B],None,None,0,0,0,False)




for i in range(m):
    rs.AddLine(A1[i],B1[i])
    rs.AddLine(B1[i],C1[i])
