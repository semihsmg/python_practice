class Calculator(object):
    def __init__(self, w=None, q=None):
        self.w = w
        self.q = q
        self.object = object

    def power(self, q, w):
        if self.q < 0 or self.w < 0:
            return 'n and p should be non-negative'
        else:
            return q ** w


myCalculator = Calculator()
n, p = map(int, input().split())
try:
    ans = myCalculator.power(n, p)
    print(ans)
except Exception as e:
    print(e)
