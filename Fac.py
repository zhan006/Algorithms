def fac(n):
    if n == 1 or 0:
        return 1
    else:
        return n * fac(n - 1)


def test():
    print(fac(5))

test()