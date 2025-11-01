# Generators
# Allows to generate a sequence of values over time

# Example of a builtin generator is range(100)

# Generators are iterable (but not all iterables are generators)

# def generator_function(num):
#     for i in range(num):
#         yield i*2       # yield pauses the function


# g = generator_function(100)
# print(next(g))
# print(next(g))
# print(next(g))
# next gets the next value from the generator function
# until we are out of values
# next(g) after 99 will raise a StopIteration exception

# Example: how does a for loop work under the hood:
def special_for(iterable):
    iterator = iter(iterable)   # iter is a generator and creates an iterator object
    while True:
        try:
            print(iterator)
            print(next(iterator))   # grab the next item from the list
        except StopIteration:       # when we there are no more items in the list
            break                   # break out of the while


special_for([1, 2, 3])


# Example: create a range function
class MyGen():
    # current = 0
    # the original example uses a class variable, but not sure why?
    # it also ignores the first value provided in the __init__...

    def __init__(self, first, last):
        self.first = first
        self.current = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.last:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for i in gen:
    print(i)
