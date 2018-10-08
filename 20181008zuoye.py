


'''
#1
def getPentagonalNumber(n):
    for i in range(1,101):
        for x in range(i):
            a=x*(3*x-1)/2
            print(a,end = '')
        print(i*(3*i-1)/2)

'''

'''
#2
def sumDigits(n):
    s=0
    while n!=0:
        s=s+n%10
        n=n/10
    return s
a=eval(raw_input('>>>'))
print(sunDigits(a))

    

'''
    
'''
#3



def displaySorteNumbers(num1,num2,num3):
    if num1 > num2:
        num1,num2=num2,num1
    if num2 > num3:
        num2,num3=num3=num2
    if num1 > num2:
        num1,num2=num2,num1
    return num3,num2,num1



a,b,c=eval(raw_input('enter three number'))
print(displaySorteNumbers(a,b,c))

'''


'''
#4

def futureInvestmentValue(a,b):
    b=b*0.01
    y=a*(1+1*b)
a,b=eval(raw_input())
s=0
for i in range(0,30):
    i+=1
    
    print(i,futureInvestmentValue(a,b))

'''

'''
#5
import math
def printChars(ch1,ch2,numberPerLine):
    for i in range(1,ord(ch2)-ord(ch1)):
        print('{} '.format(chr(ord(ch1)+i)),end='')
        if i%numberPerLine==0:
            print()
s1='1'
s2='Z'
n=10
printChars(s1,s2,n)

'''

'''

#6
for p in range(1,32):
    fg=0
    if 2**p-1==1:
        continue
    for i in range(2,2**p-1-1):
        if (2**p-1)%i==0:
            fg=1
            break
    if fg==0:
        print(p,' ',2**p-1)



'''

'''

#7

import time
now=time.time()
mon=time.localtime(now)[1]
day=time.localtime(now)[2]
year=time.localtime(now)[0]
hour=time:w.localtime(now)[3]
mins=time.localtime(now)[4]
sec=time.localtime(now)[5]
print('Current date and time is '+str(mon)+' '+str(day)+','+str(year)+' '+str(hour)+':'+str(mins)+':'+str(sec))

'''

'''

#8


import random
a=random.randint(1,6)
b=random.randint(1,6)
n=a+b
if n==2 or n==3 or n==12:
    print('You rolled ',a,'+',b,'=',n)
    print('You lose')
elif n==7 or n==11:
    print('You rolled ',a,'+',b,'=',n)
    print('You win')
else:
    print('You rolled',a,'+',b,'=',n)
    print('point is ',n)
    i=n
    while i!=7:
        x=random.randint(1,6)
        y=random.randint(1,6)
        m=x+y
        if i==m :
            print('You rooled ',x,'+',y,'=',m)
            print('You win')
            break
        elif m==7:
            print('You rooled ',x,'+',y,'=',m)
            print('You loss')
            break
        else:
            print('You rooled ',x,'+',y,'=',m)
            print('point is ',m)
        i=m

'''

#9

























