# Square
my_list = [5, 4, 3]

print(list(map(lambda x: x**2, my_list)))

# List sorting (on the second item)
a = [(0,2), (4,3), (9,9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)