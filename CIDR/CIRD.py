import sys

def numericals(s):
    return [ int(i,2) for i in s ]

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
    n = int(n)

    if len(sys.argv)>2:
        if sys.argv[2]=='n':
            c = toBinary(ci.split('.'))
        else :
            c = ci.split('.')
    else:
            c = toBinary(ci.split('.'))

    first, last = getFirstLast(c,n)
    
    print('\n')
    print('Binary')
    print('Original : ',c)
    print('First    : ',first)
    print('Last     : ',last)

    print('\n')
    print('Numericals')
    print('Original : ',numericals(c))
    print('First    : ',numericals(first))
    print('Last     : ',numericals(last))

    print()
    print('Number   : ',2**(32-n))

if __name__=='__main__':
    main()
