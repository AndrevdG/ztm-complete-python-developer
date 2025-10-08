# # Fundamental Datatypes
# int
# float
# bool
# str
# list
# tuple
# set
# dict

# # Classes -> custom types

# # Specialized datatypes

# None

# print(type(2 + 4))
# print(type(2 - 4))
# print(type(2 * 4))
# print(type(2 / 4))

# print(2 ** 2)   # power of
# print(3 // 4)   # DIV
# print(5 % 4)    # MOD

# math functions
# print(round(3.1))
# print(abs(-3.1))

# operator precedence -> (), **, * /, + -

# complex
# complex

# # convert int to binary
# print(bin(5))
# # convert binary to int
# print(int('0b101', 2))

# # augmented assignment operator
# some_value = 5
# some_value += 2
# print(some_value)

# string1 = 'single quotes'
# string2 = "double quotes"
# long_string = '''
# WOW
# O O
# ---
# '''
# print(long_string)
# first_name = 'Andre'
# last_name = 'van der Goes'
# full_name = first_name + ' ' + last_name
# print(full_name)

# print('hello ' + str(5))

# Escape sequence
# weather = 'It\'s sunny'
# print(weather)
# \t -> tab
# \n -> newline

# # formatted strings
# name = 'Joe'
# age = 5
# # preferred way
# print(f'Hello {name}, you are {age} years old')
# # python 2 way
# print('Hello {}, you are {} years old'.format(name, age))
# print('Hello {1}, you are {0} years old'.format(age, name))

# [start:stop:stepover]
# [1:] go from 1 to end
# [:5] go from 0 to 5
# [::2] go from start to end, step over one
# [-1] start from end
# [::-1] reverse order (0 to end, step -1)

# test = 'abcdefg'

# # slicing
# print(test[0])
# print(test[5])
# print(test[1:6:2])

# strings are immutable
# test[0] = 'c' <--- fails because we cannot change a character in an (immutable) string

# username = input('Username: ')
# password = input('Password: ')
# password_length = len(password)
# print(f'{username}, your password: {'*' * password_length} is {password_length} characters long')

# Lists
# li = [1, 2, 3, 4, 5]
# li2 = ['a', 'b', 'c', 'd']
# li3 = [1, 2, 'a', True]

# amazon_cart = ['notebook', 'sunglasses']
# print(amazon_cart[1])

# # List slicing
# amazon_cart = [
#     'notebook',
#     'sunglasses',
#     'toys',
#     'grapes'
# ]

# print(amazon_cart[0::2])
# amazon_cart[0] = 'laptop'

# new_cart = amazon_cart[0:3]     # slicing creates a new list
# new_cart = amazon_cart          # points new_cart to the same memory point as amazon_cart
# new_cart = amazon_cart[:]       # returns a new list with all items of amazon_cart

# matrix; list in list (multidimensional)
# matrix = [
#     [1, 2, 3],
#     [2, 4, 6],
#     [5, 2, 7]
# ]

# print(matrix[1][2])

# basket = [1, 2, 3, 4, 5]

# # adding
# new_list = basket.append(100)
# print(new_list)     # New list is None because append edits the list in place and does not return anything
# print(basket)
# basket.insert(4, 105)
# basket.extend([100, 101])
# basket.pop()    # pops off the end of the list, returns and removes
# basket.pop(0)   # pops off at the index
# basket.remove(3)    # removes item at index
# basket.clear()  # removes all items

# basket = ['a', 'b', 'c', 'd']
# print(basket.index('b'))
# basket.index('b', 0, 3)     # find the index of 'b', between indexes 0 and 3
# # index throws an error if the item is not in list.
# 'b' in basket   # true if 'b' in list
# basket.sort()   # sorts items in basket in place (list is changed)
# sorted(basket)  # returns a sorted list, but the list is not changed

# basket.reverse()    # reverse the list in place
# basket[::-1]        # returns a new list with the items reversed

# range(1, 100)         # outputs range from 1 to 99
# range(100)            # outputs range from 0 to 99

# sentence = '!'
# new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'slim', 'shady'])
# print(new_sentence)     # hi!my!name!is!slim!shady
# new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'slim', 'shady'])
# print(new_sentence)     # hi my name is slim shady

# # list unpacking
# a, b, c = [1, 2, 3]     # a = 1, b = 2, c = 3
# a, b, c, *other = [1, 2, 3, 4, 5, 6]     # a = 1, b = 2, c = 3, other = [4, 5, 6]
# a, b, c, *other, d = [1, 2, 3, 4, 5, 6]     # a = 1, b = 2, c = 3, other = [4, 5], d = 6

# # dictionaries - dictionaries are orders since python 3.7
# dictionary = {
#     "a": 1,
#     "b": 2
# }

# print(dictionary["b"])

# # Both lists and dictionary can contain other data structures
# new_dictionary = {
#     "a": [1, 2, 3],
#     "b": "Hello",
#     "x": True
# }

# new_list = [
#     {
#         "a": [1, 2, 3],
#         "b": "Hello",
#         "x": True
#     },
#     {
#         "a": [4, 5, 6],
#         "b": "Hello",
#         "x": True
#     }
# ]

# print(new_list[1]['a'][2])

# # dictionary keys need to be immutable
# #   - string
# #   - boolean
# #   - int
# #   - etc

# user = {
#     'basket': [1, 2, 3],
#     'greet': 'hello'
# }

# # accessing dictionary items by using .get prevents exception, returns None if key does not exist
# # you can also provide a value to be inserted as default value
# print(user.get('age', 'default'))

# # # alternative (not much used) way to create a dictionary
# # user2 = dict(name='John')
# # print(user2)

# # you can use 'in' on dictionaries too:
# print('basket' in user)

# # Other methods:
# print('greet' in user.keys())   # access all keys
# print('hello' in user.values())   # access all values
# print(user.items())   # return all pairs as tuples
# user.clear()            # remove all items
# print(user)
# user2 = user.copy()         # copies dictionary to another dictionary
# print(user.pop('greet'))    # returns a value and remove from dictionary
# print(user.popitem())         # returns the last key/value in the dictionary (since python 3.7)
# print(user.update({'age': 55}))     # update key/value pair or add one if the key does not exist

# Tuple -> tupples are immutable

# Generally:
# Use lists where you have a mutable number of items
# (if you need to add, remove or modify items from a list and use the list itself afterwards).
# Use tuples if you have a fixed number of items at the time of the creation of the tuple.
# You won’t be able to modify and use it again later, though
# (that would require creating a new tuple, which would probably defeat the optimization effort)

# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[1])
# print(5 in my_tuple)
# # you can slice a tuple. With a single item, it will return
# # (2,) -> still a tuple
# new_tuple = my_tuple[1:2]
# print(new_tuple)

# x, y, z, * other = (1, 2, 3, 4, 5)
# print(x)        # 1
# print(other)    # [4, 5]    (list!)

# Sets: brackets like a dictionary but single items
# Sets only store unique items

# my_set = {1, 2, 3, 4, 5, 5}     # print: {1, 2, 3, 4, 5}
# my_set.add(100)     # added
# my_set.add(2)       # not added, already there

# print(my_set)

# # set function
# my_list = [1, 2, 3, 4, 5, 5]
# print(set(my_list))             # get the unique items from the list

# # No indexing: my_set[0] throws

# print(1 in my_set)
# print(len(my_set))      # length = 5, no duplicates

# new_set = my_set.copy()     # copies the set


my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# print(my_set.difference(your_set))      # {1, 2, 3}

# my_set.discard(5)
# print(my_set)                           # {1, 2, 3, 4}

# my_set.difference_update(your_set)
# print(my_set)                           # {1, 2, 3} -> the set is modified, not the return values

print(my_set.intersection(your_set))      # {4, 5}

