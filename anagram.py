def number_needed(a, b):
    arr = []
    la = len(a)
    lb = len(b)

    for i in a:
        if i in b:
            p = b.find(i)  # for index of the char
            arr.append(i)
            b = b[:p] + b[(p + 1):]
            # b = b.replace(i, '')  # replaces all occurrence of i
        else:
            pass

    # print(b)
    # print(count)
    # print(arr)

    return la + lb - (len(arr) * 2)


x = input().strip()
y = input().strip()

print(number_needed(x, y))
