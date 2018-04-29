from datetime import datetime


def time_conversion(s):
    t1 = datetime.strptime(s, '%I:%M:%S%p')
    return str(datetime.strftime(t1, '%H:%M:%S'))


print(time_conversion(input()))
