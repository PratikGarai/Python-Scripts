def perm(s,n):
    for i in range(n,len(s)):
        if(n== len(s)-1):
            print(s)
        else:
            s[n],s[i] = s[i],s[n]
            perm(s,n+1)
            s[n],s[i] = s[i],s[n]

def main():
    a= ['a','b','c','d']
    perm(a,0)

main()