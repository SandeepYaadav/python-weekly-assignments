# Using below list and enumerate(), print index followed by value.
# Input: fruits = ["apple", "banana", "cherry"]
# Output:
# 0 apple
# 1 banana
# 2 cherry
fruits = ["apple", "banana", "cherry"]
for x, element in enumerate(fruits):
    print(x, element)





# Using below dict and enumerate, print key followed by value
# Input: person = {"name": "Alice", "age": 30, "city": "New York"}
# Output:
# name: Alice
# age: 30
# city: New York
person = {"name": "Alice", "age": 30, "city": "New York"}
for x, (key, value) in enumerate(person.items()):
    print(f"{key}, {value}")



# Given the list fruits = ["apple", "banana", "cherry", "date", "elderberry"], use enumerate() to create a list of tuples where each tuple contains the index and the corresponding fruit, but only for even indices.
# Output:
#              [(2, 'banana'), (4, 'date')]

fruits2 = ["apple", "banana", "cherry", "date", "elderberry"]
fruitsListTupple = [(i, fruit) for i, fruit in enumerate(fruits2) if i % 2 == 0]
print(fruitsListTupple)






