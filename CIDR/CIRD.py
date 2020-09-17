import sys

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

    print(c)
    # print(f)
    # print(l)

if __name__=='__main__':
    main()
