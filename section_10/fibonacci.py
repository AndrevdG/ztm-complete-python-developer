# Attempt 1, not a generator :(
# def fib(number):
#     ultimate = 0
#     penultimate = 0
#     for i in range(0, number + 1):
#         if (i > 1):
#             current = penultimate + ultimate
#             print(current)
#         else:
#             current = i
#             print(i)
#         penultimate = ultimate
#         ultimate = current


# fib(20)

# reworked to the lesson sample:
def fib(number):
    penultimate = 0
    ultimate = 1
    for _ in range(0, number + 1):
        yield penultimate
        t = penultimate
        penultimate = ultimate
        ultimate = ultimate + t


for x in fib(20):
    print(x)
