import sys

def processed(d):
    return [d[:8],d[8:16],d[16:24],d[24:]]
    
def getFirstLast(c,n):
    s = ''.join(c)
    f = s[:n]+'0'*(32-n)
    l = s[:n]+'1'*(32-n)

    return [processed(f),processed(l)]

def toBinary(c):
    s = []
    for i in c:
        temp = bin(int(i))[2:]
        temp = '0'*(8-len(temp))+temp
        s.append(temp)
    return s

def main():
    ci = sys.argv[1]
    ci, n = ci.split('/')

    c = toBinary(ci.split('.'))
    n = int(n)

    first, last = getFirstLast(c,n)

    print(c)
    print(first)
    print(last)

if __name__=='__main__':
    main()
