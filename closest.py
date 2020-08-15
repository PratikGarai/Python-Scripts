n = int(input())
l = list(map(int,input().split()))
l = sorted(l)
le = len(l)
for i in range(le-1,-1,-1):
    su = 0
    lt = []
    for j in range(i,-1,-1):
        if(su+l[j]<=n):
            lt.append(l[j])
            su += l[j]
    print(lt)
