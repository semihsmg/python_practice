import random
import time

target = 'Merhaba!'
string = [''] * len(target)
targetArray = list(target)

i = 0
attempts = 0
while i < len(target):
    if string[i] is not target[i]:
        string[i] = chr(random.randint(32, 126))
        attempts += 1

    if string[i] is target[i]:
        i += 1

    print()
    x = 0
    while x < len(string):
        print(string[x], end='')
        x += 1

    time.sleep(.0085)
print('\n')
print('Deneme adedi: ' + str(attempts))
