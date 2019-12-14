import time
def sqaure(n):
    start  = time.time()
    for i in range(n):
        res = i **2
    end = time.time()
    print("total time taekn as ", end)
sqaure(100000)

def cube(n):
    start = time.time()
    for i in range(n):
        res = i ** 3
    end = time.time()
    print("total time taekn as ", end)
cube(100000)
