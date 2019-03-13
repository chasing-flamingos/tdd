def negative(a):
    return -a

def add(*args):
    if len(args) < 1:
        raise RuntimeError("add() needs at least one argument. None was given.")

    sum = 0
    for n in args:
        sum += n
    return sum

def substract(a, b):
    return add(a, negative(b))
