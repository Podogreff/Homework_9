def ab_func(a, b):
    try:
        a, b = int(a), int(b)
        print(a**2 / b)
    except ValueError:
        print("There is TypeError, please enter the NUMBER!")
    except ZeroDivisionError:
        print("b cant be: '0', please enter another number")


ab_func(input("Enter first number: "), input("Enter second number: "))
