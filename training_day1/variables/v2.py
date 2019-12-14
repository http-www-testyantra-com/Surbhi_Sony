a,b = 10,20
def sample1():
    x,y = 2,4
    def inner():
        global a,b
        nonlocal x,y
        a,b = b,a
        x,y = y,x
        print(x,y)
        print(a,b)
    print(x,y)
    inner()
    print(x,y)

sample1()