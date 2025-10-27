from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def to_upper(item):
    return item.upper()

print(list(map(to_upper, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

# my_numbers.reverse()
# print(list(zip(my_strings, my_numbers)))
print(list(zip(my_strings, sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def score_over_50(score):
    return score > 50

print(list(filter(score_over_50, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def my_sum(acc, num):
    return acc + num

# print(reduce(my_sum, my_numbers, reduce(my_sum, scores)))
print(reduce(my_sum, my_numbers + scores))      # Cleaner solution...