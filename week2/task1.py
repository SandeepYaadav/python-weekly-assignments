# Given a list let's see how to double each element of the given list. Using map()
from functools import reduce

a = [1, 2, 3, 4]

double = list(map(lambda x: x * 2, a))

print(double)

# Use filter() and lambda to extract all even numbers from a list of integers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# Use reduce() and lambda to find the longest word in a list of strings.
# from functools import reduce
# words = ["apple", "banana", "cherry", "date"]

words = ["apple", "banana", "cherry", "date"]

max_len_word = reduce(lambda a, b: a if len(a) >= len(b) else b, words)
print(max_len_word)

# Use map() to square each number in the list and round the result to one decimal place.
# my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

my_sq_floats = list(map(lambda x: round(x ** 2, 1), my_floats))

print(my_sq_floats)


# Use filter() to select names with 7 or fewer characters from the list.
# my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
# #Expected Output: ['olumide', 'josiah', 'omoseun']

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

my_names_with_7_or_fewer = list(filter(lambda name: len(name) <= 7, my_names))

print(my_names_with_7_or_fewer)


# Use reduce() to calculate the sum of all numbers in a list. [1, 2, 3, 4, 5]

numbs = [1, 2, 3, 4, 5]
sum = reduce(lambda a,b: a+b, numbs)
print(sum)

