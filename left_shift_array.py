from collections import deque


def array_left_rotation(arr, shift):
    items = deque(arr)
    items.rotate(-shift)
    return list(items)


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
print(*array_left_rotation(a, k), sep=' ')
