# Functional programming

# Pure functions - seperation between data of a program and behavior of a program
#
# 1. Given same input, return same output
# 2. Does not produce side effects a.k.a. no effect on the outside world (everything outside of the function):
#       - a print statement would produce a message and thus has effect on the outside world
#       - changing a global variable has effect on the outside world

# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item *2)
#     return new_list

# print(multiply_by2([1,2,3]))    # always returns [2, 4, 6], has no side effects

# ###### map, filter, zip and reduce
# # read also: https://medium.com/@f.huber/a-common-python-myth-or-why-you-dont-need-map-filter-and-reduce-in-python-0e92eeae99eb

# my_list = [1, 2, 3]
# your_list = [10, 20, 30]

# # map:
# def multiply_by2(item):
#     return item * 2

# print(list(map(multiply_by2, my_list)))   # map takes an iterable and performance an action over all items
#                                             # returning the same value as above

# # filter:
# def only_odd(item):
#     return item % 2 != 0

# print(list(filter(only_odd, my_list)))   # filter works similarly to filter data from an iterable

# # zip:
# print(list(zip(my_list, your_list)))

# # reduce
# from functools import reduce

# def accumulator(acc, item):
#     print(acc, item)            # just so we can follow, not a pure function anymore ;-)
#     return acc + item

# print(reduce(accumulator, my_list, 0))
# print(my_list)

# ##### lambda expressions
# # use once, anonymous functions
# # 
# # lambda param: action(param)

# print(list(map(lambda item: item*2, my_list)))

# print(list(filter(lambda item: item % 2 != 0, my_list)))

# print(reduce(lambda x, y: x + y, my_list, 0))

##### list, set, dict comprehensions

# my_list = [param for param in iterable]

# my_list = [char for char in 'hello']
# my_list2 = [num for num in range(0, 100)]
# my_list3 = [num**2 for num in range(0, 100)]
# my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]

# print(my_list4)

## set works the same as list above
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {k:v**2 for k,v in simple_dict.items() if v % 2 == 0}

my_dict2 = {num:num*2 for num in [1, 2, 3]}

print(my_dict2)