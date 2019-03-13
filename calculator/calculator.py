def negative(a):
    return -a

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

def substract(a, b):
    return add(a, negative(b))
