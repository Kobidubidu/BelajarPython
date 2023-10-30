def f(n):
    import time
    if n == 0:
        print('dadah!')
        return
    print(n, end='')
    time.sleep(0.5)
    f(n-1)
f(15)
