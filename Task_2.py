def ab_func(a, b):
    try:
        a**2 / b
        print(a**2 / b)
    except TypeError:
        print("There is TypeError, please enter 'INT'")
    except ZeroDivisionError:
        print("b cant be: '0', please enter another number")


ab_func("23", 3)
