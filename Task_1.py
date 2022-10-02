def oops():
    name = "Vlad"
    print(name[4])

def new_oops():
    try:
        oops()
    except IndexError:
        print("Hello, IndexError =)")


new_oops()
