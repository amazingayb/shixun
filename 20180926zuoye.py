

'''
#.1

import math
a=float(raw_input('r>>'))
s=(2*a)*math.sin(3.14/5)
AREA=(5*s*s)/(4*math.tan(3.14/5))
print("area is %.2f"%AREA)
'''

'''
#.2
import math
x1,y1=eval(raw_input("latitude and longitude"))
x2,y2=eval(raw_input("latitude and longitude"))
a=math.sin(math.radians(x1))*math.sin(math.radians(x2))
b=math.cos(math.radians(x1)*math.cos(math.radians(x2)))
c=math.cos(math.radians(y1-y2))
d=6371.01*math.acos(a+b*c)
print(d)
'''


'''
#.3
import math
s=float(raw_input("Enter the side"))
a=5*s*s
b=4*math.tan(math.pi/5)
area=a/b
print(area)
'''

'''

#.4
import math
a,b=eval(raw_input("enter number of side and side "))
x=a*b*b
y=4*math.tan(math.pi/a)
area=x/y
print(area)

'''

'''
#.5
a=int(raw_input("ACSII code"))
b=chr(a)
print(b)
'''

'''
#.6
a,b,c,d,e=eval(raw_input("name",end=" ""time",end" ""pay",end" ""federal withholding rate",end" ""state withholding rate",end" "))
x=
'''

'''
#.7

a=raw_input("enter a integer")
print("the number is"+a[::-1])
'''

'''

#.8

import hashlib
str1 = 'this is a test.'
h1 = hashlib.md5()
h1.update(str1.encode(encoding = 'utf-8'))
print('MD5', h1.hexdigest())
'''

'''
#.9

import math

a,b,c=eval(raw_input("enter a,b,c"))
x=b*b-4*a*c
r1=((-1*b)+math.sqrt(b*b-(4*a*c)))/2*a
r2=((-1*b)-math.sqrt(b*b-(4*a*c)))/2*a
if x>0:
    print("the roots are",r1,r2 )
elif x==0:
    print("the root is",r1)
else:
    print("no root")
'''

'''
#.10

import random

a=random.randint(0,100)
b=random.randint(0,100)
c=a+b
print(str(a),str(b))
d=eval(raw_input("qing shu ru liang ge shu de he "))
if d==c:
    print("True")
else:
    print("False")
'''


'''
#.11

a=raw_input("today is")
if a<7:

    elif a==0:
        print("today is sunday")
    elif a==1:
        print("today is monday")
    elif a==2:
        print("today is tusday")
    elif a==3:
        print("today is wednesday")
    elif a==4:
        print("today is thursday")
    elif a==5:
        print("today is friday")
    elif a==6:
        print("today is saturday")


'''

















































































































