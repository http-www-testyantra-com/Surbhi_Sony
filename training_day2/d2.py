import time
def timer(func):
    def inner(n):
        start = time.time()
        func(n)
        end = time.time()
        print("total time taken as", end)
        return inner

    @timer
    def cube(n):
        for i in range(n):
            res = i ** 3
    @timer
    def sqaure(n):
        for i in range(n):
            res = i ** 2

