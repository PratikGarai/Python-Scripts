b= []
x=[1,7,9]
n = 15
def fun(a):
    for i in x:
        if(sum(a) +i ==n):
             print (a+ [i])
        elif(sum(a) + i >n):
            return
        else:
            fun(a+[i])

fun(b)