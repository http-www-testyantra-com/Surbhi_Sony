def get_input():
    try:
        a = int(input("enter value "))
        b = int(input("enter value "))
        return a,b
    except ValueError as e:
        print(e)
        return get_input()

    finally:
        print("finally of get_input")

def div(a,b):
    try:
        c = a / b
        return c
    except ZeroDivisionError as e:
        print(e)
        return div(a,b)

    finally:
        print("finally of div")

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