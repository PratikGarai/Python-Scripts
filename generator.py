def func():
    for i in range(10):
        yield i

a = func()
while(True):
    try:
        print(next(a))
    except:
        print('Done')
        break
