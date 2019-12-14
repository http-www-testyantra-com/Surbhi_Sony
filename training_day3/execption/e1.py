def get_input():
    a = int(input("enter value "))
    b = int(input("enter value "))
    return a,b

def div(a,b):
    c = a/b
    return c

def main():
    a,b = get_input()
    c = div(a,b)
    print(c)

if __name__ == "__main__":
    main()