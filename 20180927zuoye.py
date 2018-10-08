#.1



















#.2


#a=((1+0.05)*(10000)) #first year cost
#b=((1+0.05)*a) #second year cost
#c=((1+0.05)*b) #third year cost
#d=((1+0.05)*c) #forth year 
a=10000
i=1
while i<4:
    a=((1+0.05)*a)
    i+=i
print(a)
