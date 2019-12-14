def s(a,b,c):
    print(a,b,c)


print(s(*"abc"))
print(s(*[1,2,3]))
print(s*(1,2,3))
print(s*{1,2,3})
print(s(*{"a":1, "b":2, "c":3}))
print(s(**{"a":1, "b":2, "c":3}))
