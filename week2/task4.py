# Find the Maximum and Minimum Values in a List
# numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]
print(min(numbers))
print(max(numbers))



# Given a set of numbers, find the maximum and minimum values.
# setn = {5, 10, 3, 15, 2, 20}
setn = {5, 10, 3, 15, 2, 20}
print(min(setn))
print(max(setn))



# Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and longest word from the list, in that order. If there are multiple words of the same shortest or longest length, return the first shortest/longest word found.
# Input: words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
# Output: ('kiwi', 'grapefruit')
def find_largest_and_shortest_string():
    str_list = input("Enter the fruits: ").split(" ")
    shortest = min(str_list, key=len)
    longest = max(str_list, key=len)
    return (shortest, longest)

print(find_largest_and_shortest_string())

