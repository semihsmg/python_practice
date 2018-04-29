n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numberOfSwaps = 0
for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            x = a[j + 1]
            a[j + 1] = a[j]
            a[j] = x
            numberOfSwaps += 1
    if numberOfSwaps is 0:
        print('x')

print('Array is sorted in ' + str(numberOfSwaps) + ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[n - 1]))

print(a)
