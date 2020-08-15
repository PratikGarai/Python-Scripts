main = [1,2,5,6,9]
k = 8
def sums(n, a):
    b = a
    if(n==len(main)):
        return
    l = main[n]
    s1 = sum(b + [l])
    if(s1 == k):
        print (b + [l])
    sums(n+1,a)
    sums(n+1, a+ [l])

c=[]
sums(0,c)