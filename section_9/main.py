# Error handling

# Example exception ;)
# print(1+'hello')        # TypeError

while True:
    try:
        age = int(input('what is your age? '))
        print(age)
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter a number greater than 0!')
    else:
        print('thank you!')
        break
    finally:
        print('ok, finally done with you')


def my_error():
    # raise ValueError
    raise Exception('hey cut it out!')    # We can raise our own exceptions as well


# def sum(num1, num2):
#     try:
#         return num1 + num2
#     except TypeError as err:
#         print(f'please enter numbers {err}')    # add a descriptive message to the error


# print(sum('1', 2))

# def sum(num1, num2):
#     try:
#         return num1 / num2
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)


# print(sum(1, 0))
