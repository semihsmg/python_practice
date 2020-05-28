# def fact(x):
#     if x == 1:
#         return 1
#     else:
#         return x * fact(x-1)


def go(n, a):
    if n > 1:
        m = n - 1
        a = a * n
        return go(m, a)
    else:
        return a


# print(fact(10))
print(go(10, 1))
