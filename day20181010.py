
'''


a='http//:www.baidu.com/?pang='
b=1000
c='wd=xioapangzi'
for i in range(100):
    i+=1
    print(a,i,c)

'''


'''


A2=[1,1,1,1,2,2,2,2,3,3,]
a=[]
for i in A2:
    if i not in a:
        a.append(i)
print(a)

'''






a4 = [['liuyanyun',22,['360',100]],['jingjing',12,['baidu',1]],['taotao',-1,['Google',50]]]
a4.sort(key=lambda x:x[2][1])
print(a4)





file = open('your file path',encoding='gbk',errors='ignore')
file.readline()
file.close()
file = open('your file path','a',encoding='gbk',errors='ignore')



while 1:
    line = file.readline()
    if '刘伟东' in line:
        print(line)
