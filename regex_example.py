import re

firstName = []
emailID = []
selected = []


def rx(name, mail):
    for m in mail:
        if re.search(r'@gmail.com', m):
            index = mail.index(m)
            selected.append(name[index])
    selected.sort()


N = int(input().strip())
for _ in range(N):
    fn, eid = input().strip().split(' ')
    firstName.append(fn)
    emailID.append(eid)

rx(firstName, emailID)

print(firstName)
print(emailID)
print('\n'.join(selected))
