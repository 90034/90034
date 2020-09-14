# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


print('解一元二次方程式:')
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

x=(b**2)-(4*a*c)

if x<=0:
    print('無解')

else:
    x1=(-b+(b**2-4*a*c)**0.5)/(a*2)
x2=(-b-(b**2-4*a*c)**0.5)/(a*2)
print('x1=',x1)
print('x2=',x2)