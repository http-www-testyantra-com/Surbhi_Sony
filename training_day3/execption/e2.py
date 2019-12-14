def get_input():
    a = int(input("enter value "))
    b = int(input("enter value "))
    return a,b

def div(a,b):
    c = a/b
    return c

def main():
    try:
        a,b = get_input()
        c = div(a,b)
        print(c)
    except ZeroDivisionError as e:
        print(e)
        main()

    except Exception as e:
        print(e)
        main()

    except:
        print("exception has raised")


if __name__ == "__main__":
    main()