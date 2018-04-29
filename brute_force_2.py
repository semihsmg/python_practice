import random
import time

target = 'Bu cümleyi yazmam için geçen süre ve deneme adedi:'
string = [''] * len(target)
targetArray = list(target)

i = 0
attempts = 0
start_time = time.time()
while i < len(target):
    if string[i] is not target[i]:
        # select random ASCII character between 32-254
        string[i] = chr(random.randint(32, 254))
        attempts += 1

    if string[i] is target[i]:
        i += 1

    # print()
    # x = 0
    # while x < len(string):
    #     print(string[x], end='')
    #     x += 1
    #
    # time.sleep(.05)

elapsed_time = time.time() - start_time
print('\n' + ''.join(string))
print('\n' + 'Sure: ' + str(elapsed_time))
print('Deneme: ' + str(attempts))
