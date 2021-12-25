def find(s):
     m = []
     k = len(s)
     for i in range(0,k):
          for j in range(i+1,k+1):
               m.append(s[i:j])
     return m
          
def main():
     a = input()
     b = input()
     la = sorted(find(a))
     lb = sorted(find(b))
     maxlen = -1
     res = ''
     for i in la:
          for j in lb:
               s = i+j
               k = len(s)
               if(s==s[::-1]):
                    if(k>maxlen):
                         res= s
                         maxlen = k
     if(maxlen!=-1):
          print(res)
     else:
          print(-1)
main()

          
                    
