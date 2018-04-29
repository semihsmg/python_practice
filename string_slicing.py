n = int(input().strip())  # number of string you want to enter
arr = []

# print(n)
# print(arr)

for x in range(n):  # fill the arr
    arr.append(str(input().strip()))

for x in arr:  # slice it!
    print(str(x[::2]) + '  ' + str(x[1::2]))
