def generate(n):
    for i in range(n):
        yield i


numbers = generate(5)

print(numbers)
print(list(numbers))
print(list(numbers))
