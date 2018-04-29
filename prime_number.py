def is_prime(num):
    # only even prime number
    if num is 2:
        return True

    # 0 and 1 are not primes
    if num < 2:
        return False

    # top limit for loop is the square root of the number + 1
    limit = int(num ** 0.5) + 1

    if num % 2 is 0:
        return False

    for i in range(3, limit, 2):
        if (num % i) is 0:
            return False

    return True


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

for x in arr:
    if is_prime(x):
        print('Prime')
    else:
        print('Not prime')
