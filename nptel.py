a = list(map(int,input().split()))
l = a[0]
n = a[1]
arr = [int(input()) for i in range(l)]
negs = []
#ignore negs from front and back
start = 0
end = l-1
while(arr[start]<0):
    start+= 1
while(arr[end]<0):
    end -= 1
sumglobal = -100000000
sumlocal = 0
negs = []
lnegs = 0
negsum= 0
possum= 0
for i in range(start,end+1):
    if arr[i]<0:
        negs.append(arr[i])
        negs = sorted(negs)
        lnegs += 1
        if(n>=lnegs):
            negsum = 0
        else:
            negsum = sum(negs[n:])
    else:
        possum += arr[i]
    sumlocal = possum+negsum
    if(sumlocal>sumglobal):
        sumglobal = sumlocal
    if(sumlocal<0):
        sumlocal = 0
        possum = 0
        negsum = 0
        lnegs = 0
        negs = []
if(sumglobal<0 and ( 0 in arr)):
    sumglobal = 0
print(sumglobal)
