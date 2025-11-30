# 1 . Write a Python program to read the entire content of a file named sample.txt and display it.
import csv
import functools

with open('sample.txt', 'r') as file:
    size_to_read = 20

    f_content = file.read(size_to_read)
    while len(f_content) > 0:
        print(f_content)
        f_content = file.read(size_to_read)

# 2. Write a Python program to count the number of words in a file named words.txt
with open('words.txt', 'r') as file:
    text = file.read()
    words = text.split()  # Split on whitespace
    print(f'Total number of words : {len(words)}')



# 3.Create a program to write the string “Hello, Python!” into a file named output.txt.
with open('output.txt','w') as file:
    file.write('Hello, Python!')


# 4. Write a Python program to create a CSV file named students.csv with columns Name, Roll Number, and Marks. Add at least three entries
#
# 	data = [
#     ["Name", "Roll Number", "Marks"],
#     ["Alice", "101", "85"],
#     ["Bob", "102", "90"],
#     ["Charlie", "103", "88"]
# ]


data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("students.csv created successfully!")

# 5. From a file with 100+ lines. Write a code using a generator to fetch all the data from the file.
def read_file_generator(filename):
    with open(filename, "r", newline='') as file:
        for line in file:
            yield line   # yield one line at a time

for line in read_file_generator("sample.txt"):
    print(line)



