class Difference:
    def __init__(self, a):
        self.maximumDifference = 0
        self.__elements = a

    def computeDifference(self):
        x = sorted(self.__elements)
        self.maximumDifference = abs(x[len(x) - 1] - x[0])


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
