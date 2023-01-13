from math import pi
x = int(input())
def Circle():
    return pi * (x**2)
def Rhombus():
    return 1/2 * ((x*2)**2)
print('%.6f' %Circle())    
print('%.6f' %Rhombus())