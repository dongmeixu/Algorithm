def lcm(a, b):
    min_ = min(a, b)

    i = 2
    res = 0
    while not (res % a == 0 and res % b == 0):
        res = min_ * i
        i += 1
    return res