import random

arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

# Random array
# arr = []
# for arr_i in range(6):
#     arr_t = [int(random.randrange(0, 9)) for arr_temp in range(6)]  # -9 olarak degistir 0 degerini
#     arr.append(arr_t)

top, mid, bottom = [], [], []

biggest = -50
top_s, mid_s, bottom_s = 0, 0, 0

for i in range(6):  # kaldir
    print(arr[i])

print()

for i in range(4):
    for x in range(4):
        for j in range(x, 3 + x):
            top.append(arr[i][j])
            bottom.append(arr[i + 2][j])

for i in range(1, 5):
    for j in range(1, 5):
        mid.append(arr[i][j])

for _ in range(16):
    top_s, mid_s, bottom_s = 0, 0, 0
    for _ in range(3):
        top_s += top.pop(0)
        bottom_s += bottom.pop(0)
    mid_s += mid.pop(0)
    total = top_s + mid_s + bottom_s
    if total > biggest:
        biggest = total

print(biggest)

# 1 1 1   1 1 0   1 0 0   0 0 0
#   1       0       0       0
# 1 1 1   1 1 0   1 0 0   0 0 0
#
# 0 1 0   1 0 0   0 0 0   0 0 0
#   1       1       0       0
# 0 0 2   0 2 4   2 4 4   4 4 0
#
# 1 1 1   1 1 0   1 0 0   0 0 0
#   0       2       4       4
# 0 0 0   0 0 2   0 2 0   2 0 0
#
# 0 0 2   0 2 4   2 4 4   4 4 0
#   0       0       2       0
# 0 0 1   0 1 2   1 2 4   2 4 0

# 2 4 4
#   2
# 1 2 4

# Max sun 19

