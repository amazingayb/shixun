
'''
#1
def Judge(s):
    s = s.split()
    max = 0
    count = 0
    for i in range(len(s)):
        if max < int(s[i]):
            max = int(s[i])
    for i in range(len(s)):
        c = int(s[i])
        count += 1
        if c >= max -10:
            print("Student " + str(count) + " score is " + s[i] + " and grade is A")
            continue
        elif c >= max - 20:
            print("Student " + str(count) + " score is " + s[i] + " and grade is B")
            continue
        elif c >= max - 30:
            print("Student " + str(count) + " score is " + s[i] + " and grade is C")
            continue
        elif c >= max - 40:
            print("Student " + str(count) + " score is " + s[i] + " and grade is D")
            continue
        else:
            print("Student " + str(count) + " score is " + s[i] + " and grade is F")
            continue
s = input("Enter scores: ")
Judge(s)


#2
def _reverse(num):
    num = num.split()
    i = len(num) - 1
    while i >= 0:
        print(num[i], end=" ")
        i -= 1
    print("\n")
num = input("Please input a string: ")
_reverse(num)





#3



def count(num):
    num = num.split()
    count = []
    for q in range(0, 101):
        count.append(0)
    for i in range(len(num)):
        count[int(num[i])] += 1
    for i in range(1, 101):
        if count[i] != 0:
            if count[i] == 1:
                print(str(i) + " occurs " + str(count[i]) + " time")
            else:
                print(str(i) + " occurs " + str(count[i]) + " times")
num = input("Enter integers between 1 and 100: ")
count(num)





#4



def pinjun(n):
    sum_=0
    l=len(n)
    for i in n:
        sum_ += int(i)
    return sum_/(l*1.0)

def bijiao(n):
    big=0
    small=0
    for i in n:
        if int(i)>=pinjun(n):
            big += 1
        else:
            small +=1
    print('Big:'+str(big))
    print('Small:'+str(small))

if __name__ == '__main__':
    a = raw_input('Enter sorce:')
    s=a.split()
    bijiao(s)






#5

def indexOfSmallestElement(lst):
    m=min(l)
    print(m)
    for i in range(len(l)):
        if l[i]==m:
            print(str(i)+' ',end="")
    print()



if __name__ == '__main__':
    
    a=input('>>')
    l=a.split()
    indexOfSmallestElement(l)







#6

from random import *
def shuffle(lst):
    lst = lst.split()
    tmp = []
    for i in range(0,len(lst)):
        if len(lst) != 0:
            r = randint(0, len(lst)-1)
            tmp.append(lst[r])
            lst.remove(lst[r])
    for i in tmp:
        print(i, end=" ")
    print("\n")
lst = input("Enter the number list: ")
shuffle(lst)








#7




def eliminateDuplicates(lst):
    s=[]
    for i in lst:
        if i not in s:
            s.append(i)
    print(s)

if __name__ == '__main__':
    a=raw_input('Enter ten number:')
    l=a.split()
    eliminateDuplicates(l)
'''




























