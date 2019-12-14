def iseven(n):
    return n%2 == 0

def even_number(l):
    even = []
    for i in l:
        if iseven(i):
            even.append(i)
        return even

print(even_number([1,2,3,4,5,6,7,7,8]))
