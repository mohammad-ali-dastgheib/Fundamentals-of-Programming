import time

def f(n):
    if n <= 1:
        return n
    return f(n-1) + f(n-2)

n = int(input("which step of fib? "))
t0 = time.clock()
fib = f(n)
t1 = time.clock()
print('result = ', fib, 'time = ', t1 - t0)
