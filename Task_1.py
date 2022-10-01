def oops():
    name = "vlad"
    print(name[4])


oops()


def new_oops():
    name = "vlad"
    try:
        print(name[4])
    except IndexError:
        print("oops")


new_oops()