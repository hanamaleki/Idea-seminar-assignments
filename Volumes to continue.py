import rhinoscriptsyntax as rs
import random
a = rs.AddPoint(0,0,0)
b = rs.AddPoint(0,50,50)
c = rs.AddPoint(50,0,50)
d = rs.AddPoint(50,50,0)
e = rs.AddPoint(0,50,0)

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

p1 = rs.AddPoint(x1,y1,0)
p2 = rs.AddPoint(x2,0,z2)
p3 = rs.AddPoint(0,y3,z3)
p4 = rs.AddPoint(x4,y4,50)
p5 = rs.AddPoint(x4,50,z4)
p6 = rs.AddPoint(50,y4,z4)

A = rs.AddInterpCurve([a,p3,b],3,0,None,None)
B = rs.AddInterpCurve([b,p4,c],3,0,None,None)
C = rs.AddInterpCurve([c,p6,d],3,0,None,None)
D = rs.AddInterpCurve([d,p1,a],3,0,None,None)
E = rs.AddInterpCurve([a,p2,c],3,0,None,None)
F = rs.AddInterpCurve([d,p5,b],3,0,None,None)

rs.ReverseCurve(B)
rs.ReverseCurve(D)

rs.AddLoftSrf([A,B],None,None,0,0,0,False)
rs.AddLoftSrf([C,B],None,None,0,0,0,False)
rs.AddLoftSrf([C,D],None,None,0,0,0,False)
rs.AddLoftSrf([A,D],None,None,0,0,0,False)





#