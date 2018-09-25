'''
#.1

celsius=raw_input('Enter a degree in Celsius:')
cel=float(celsius)
fahrenheit=float((9.0/5.0)*cel)+32
print(celsius,'Celsius is',fahrenheit,'Fahrenheit')
'''
'''
#.2
a,b=eval(raw_input('Enter the radius and length of a cylinder:'))
area=a*a*3.14
volume=area*b
print('the area is',area)
print('the volume is',volume)
'''

'''
#.3
a=float(raw_input('enter a value for feet:'))
num=a*0.305
print(a,'feet is',num,'meters')
'''

'''
#.4
a,b,c=eval(raw_input('Enter the amount of water in kilograms,initial temperature,final temperature:'))
q=a*(c-b)*4184
print('The energy needed is:',q)
'''

'''
#.5
a,b=eval(raw_input('rate'))
num=a*(b/1200)
print('interest',num)
'''


'''
#.6
a,b,c=eval(raw_input('v0,v1,t'))
num=(b-a)/c
print('average acceleratino',num)
'''

'''
#.7
a=float(raw_input('inter your money'))
num1=a*(1+0.00417)
num2=(num1+a)*(1+0.00417)
num3=(num2+a)*(1+0.00417)
num4=(num3+a)*(1+0.00417)
num5=(num4+a)*(1+0.00417)
num6=(num5+a)*(1+0.00417)
print('account value',num6)
'''

'''
#.8
a=float(raw_input('number'))
n1=a%10
n2=(a//100)
n3=(a//10)%10
n4=n1+n2+n3
print(n4)
'''









'''
a,b=eval(input('>>'))
print(a,b)
'''
