n = 4


def recursion_method(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursion_method(n - 1)
        print(n)


recursion_method(n)
