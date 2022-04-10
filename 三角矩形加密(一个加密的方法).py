print ('输入的字数需要是一个平方数，以便不必要的麻烦')
hlist={}
lingshi=[]
n=str(input('请输入：''(回车后查看字数)'))
origin=list(n)
while ' ' in origin:
    origin.remove(' ')
length=len(origin)
print (origin)
print ('当前字数：',length,',输入Y进行加密,输入N继续添加')
judge=str(input('here:'))
while judge=='N':
    nel=str(input('请输入：''(回车后查看字数)'))
    elorigin=list(nel)
    origin+=elorigin
    while ' ' in origin:
        origin.remove(' ')
    length=len(origin)
    print (origin)
    print ('当前字数：',length,',输入Y进行加密，输入N继续添加')
    judge=str(input('here:'))
print (origin)
i=int(length**0.5)
print('i=',i)
input('...')
for p in range(1,i+1):
    hlist['list'+str(p)]=lingshi
for x in range(1,i+1):
    print('x=',x)
    input('...')
    for y in range(x):
        print('y=',y)
        input('...')
        d=origin.pop(0)
        lingshi.append(d)
    zifu=''.join(lingshi)
    print(lingshi)
    name='list'+str(x)
    hlist[name]=zifu
    lingshi.clear()
for x in range(i+1,2*i+1):
    print('x=',x)
    input('...')
    for y in range(x):
        print('y=',y)
        input('...')
        d=origin.pop(0)
        lingshi.append(d)
    zifu=''.join(lingshi)
    print(lingshi)
    name='list'+str(x)
    hlist[name]=zifu
    lingshi.clear()
    


