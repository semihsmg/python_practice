import math


def grading_students(g):
    for i in range(len(g)):
        # rounded = int(round(g[i] / 5.0) * 5.0)
        rounded = int(math.ceil(g[i] / 5.0) * 5.0)
        reminder = rounded - g[i]
        print(rounded)
        print(reminder)
        if reminder < 3:
            if g[i] >= 38:
                g[i] = rounded
        else:
            pass
    return g


grades = []

for _ in range(int(input())):
    grades_item = int(input())
    grades.append(grades_item)

print(grading_students(grades))
