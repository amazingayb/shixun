'''

#1
class Account:
    def __init__(self,id_ = 0,balance_ = 100,Rate = 0):
        self.__id = id_
        self.__balance = balance_
        self.__Rate = Rate      
    def getMRate(self):
        a=(self.__Rate/12)/100
        print(a)
    def getMI(self):
        a=self.__balance*(Rate/12)
        print(a)
    def withdraw(self):
        a=eval(raw_input())
        b=self.__balance-a
        print(b)
    def deposit(self):
        a=eval(raw_input())
        b=self.__balance+a
        print(b)
    
    def show(self):
        print()

Account(1122,20000,4.5).withdraw()
acc=Account(1122,20000,4.5)
acc.getMRate()
acc.getMI()
Account(1122,20000,4.5).deposit()
acc=Account(1122,2000,4.5)
acc.getMRate()
acc.getMI()



'''

'''

#2

import math

class RP():
    def __init__(self,n,side,x,y):
        self.n = n
        self.side = side 
        self.x = x
        self.y = y
    def getP(self):
        a=self.n*self.side
        print(a)
    def getA(self):
        a=(self.n*self.side*self.side)/(4*(math.tan(3.14/self.n)))
        print(a)




RP(10,4,5.6,7.8).getP()
RP(10,4,5.6,7.8).getA()

'''


'''

#3
class Fan():
    def __init__(self,speed=1,on=False,radius=5,color='blue'):
        self.speed = speed
        self.on = on 
        self.radius = radius
        self.color = color
    def p(self):
        print(self._fan__speed,self._fan__radius,self._fan__color,self._fan__on)
fan(3,True,10,'yellow').p()
fan(2.False,5,'blue')

'''

'''

#4
class LE:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def getx(self):
        x = ((self._LE__e*self._LE__d)-(self._LE__b*self._LE__f))/((self._LE__a*self._LE__d)-(self._LE__b*self._LE__c))
        print(x)
    def gety(self):
        y = ((self._LE__a*self._LE__f)-(self._LE__e*self._LE__c))/((self._LE__a*self._LE__d)-(self._LE__b*self._LE__c))
        print(y)
a,b,c,d,e,f = eval(raw_input(">>"))
if a*d-b*c==0:
    print("no")
else:
    LE(a,b,c,d,e,f).getx()
    LE(a,b,c,d,e,f).gety()


'''

'''


#5
import math
class LE:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def getx(self):
        x = (self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
        print(x)
    def gety(self):
        y = (self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
        print(y)
x1,y1,x2,y2=eval(raw_input("Enter the endpoints of the first line segment:"))
x3,y3,x4,y4=eval(raw_input("Enter the endpoints of the second line segment:"))
a = y1 - y2
b = x2 - x1
e = x2*y1-x1*y2
c = y3 - y4
d = x4 - x3
f = x4*y3-x3*y4
if a*d-b*c==0:
    print("no")
else:
    LE(a,b,c,d,e,f).getx()
    LE(a,b,c,d,e,f).gety()



'''


































