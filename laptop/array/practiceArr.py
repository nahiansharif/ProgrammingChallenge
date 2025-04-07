lst = [1, 9, 2, 7, 8, 3, 2, 4, 6, 6, 1, 8, 9, 1, 7, 8, 5]
lst.sort()
print(lst)


res = list(filter(lambda x: x % 2 != 0, lst))
print(res)