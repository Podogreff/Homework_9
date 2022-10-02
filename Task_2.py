def ab_func(a, b):
    try:
        print(a**2 / b)
    except TypeError:
        print("There is TypeError, please enter 'INT'")
    except ZeroDivisionError:
        print("b cant be: '0', please enter another number")


ab_func(4, 0)
