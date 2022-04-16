import numpy as np
class pers:
    data1 = 0
    data2 = 0

    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2


a1 = pers(2, 0)
a2 = pers(3, 10)
a3 = pers(6, 3)
a4 = pers(8, 1)
arr = [a1, a2, a3, a4]
next(x for x in arr if x.data1 == 8).data2 = 17
ve = arr.index(next(x for x in arr if x.data2 == 17))
print(ve)
