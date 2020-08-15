a = input()
a = list(a)
l = len(a)
choice = int(input())
for i in range(0,int(l/2)):
    if(a[i]!=a[l-1-i]):
        if(a[i]>a[l-1-i]):
            a[l-1-i]= a[i]
            choice -= 1
        else:
            a[i]= a[l-1-i]
            choice -= 1
        if(choice==0):
            break
for i in range(0,int(l/2)+1):
    if(a[i]!='9'):
        a[i], a[l-1-i] = '9','9'
        choice -= 1
    if(choice==0):
        break
s=''
print(s.join(a))