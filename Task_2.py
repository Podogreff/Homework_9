def ab_func(a=0, b=0):
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a**2 / b)
    except ValueError:
        print("There is TypeError, please enter the NUMBER!")
    except ZeroDivisionError:
        print("b cant be: '0', please enter another number")


ab_func()
