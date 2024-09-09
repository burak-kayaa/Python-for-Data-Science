a = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])

iterator = a.__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())