a,b = 10,20
print(a,b)
def sample():
    global a,b
    print(a,b)
    a,b = b,a
    print(a,b)
print(a,b)

sample()