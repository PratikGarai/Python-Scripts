def floodfill(x,y,island):
    if(x==c or x<0 or y==r or y<0):
        return 0
    if(l[x][y]==water):
        return 0
    if(l[x][y]!=island):
        return 0
    else :
        l[x][y] = 0
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        s = sum([floodfill(x+dx[i],y+dy[i],island) for i in range(4)])
        return 1+s


x = int(input())
r = int(input())
l = [list(map(int,input().split())) for i in range(r)]
water = 0
visited_islands = [0 for i in range(x)]
area = [0 for i in range(x)]
maxarea = 0
maxind = -1
c = len(l[0])
for i in range(r):
    for j in range(c):
        if(l[i][j]!=0):
            if(visited_islands[l[i][j]-1]==0):
                print(l[i][j])
                visited_islands[l[i][j]-1]= 1
                a =  floodfill(i,j,l[i][j])
                area[l[i][j]-1] = a
                print(a)
                print()
                # if(a>maxarea):
                #     maxarea = a
                #     maxind = l[i][j]


if(maxind==-1):
    print('No islands')
else:
    print('Index',maxind)
    print('Area',maxarea)
