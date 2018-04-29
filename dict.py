n = int(input())
m = n
d = {}

while n > 0:
    np_arr = input().split(' ')
    print(np_arr)
    d[np_arr[0]] = np_arr[1]
    n -= 1

while m > 0:
    name = input()
    if name in d.keys():
        print(d.get(name))
    else:
        print('Not found')
    m -= 1

print(d)
