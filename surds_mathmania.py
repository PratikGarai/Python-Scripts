r = 0
def c(m):
    global r
    current = 1
    while(r<=m):
         if(r==0):
             yield current
             r +=1
         else:
             current = current*(m-r+1)/r
             r = r+1
             yield current

def mn():
    n = int(input( ))
    pos, neg = 0,0
    ite = c(n)
    for i in range(0,n+2):
        try:
            m = next(ite)
        except StopIteration:
            break
        if((n-i)%2==0):
            pos += m*((-1)**(n-i))*(3**(i/2))*(2**((n-i)/2))
        else:
            neg += m*((-1)**(n-i))*(3**(i/2))*(2**((n-i)/2))
    print(round(pos**2))

mn()