# map, filter, reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def double(num):
    return num * 2

results = map(double, numbers)

print(list(results))


double = lambda num: num * 2 # using lambda, this is the same as the function above double

print(list(map(lambda num: num * 3, numbers)))

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def isEven(num):
    return num % 2 == 0

print(list(filter(isEven, numbers)))

print(list(filter(lambda a : a % 2 == 0, numbers)))


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

expenses = [
    ("Dinner", 80),
    ("Car repair", 75)
]

sum = 0

for expense in expenses:
    sum += expense[1]

print(sum)

from functools import reduce

sum = reduce(lambda x, y: x + y[1], expenses, 0)

print(sum)