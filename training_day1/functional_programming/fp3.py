def add10(sal):
    return sal+(10/100)*sal

def add_sal(l):
    for i in range(len(l)):
        l[i] = add10(l[i])
        return l

print(add_sal([10,20,30]))

print(list(map(lambda sal:sal + (10/100)*sal, [10,20,30])))