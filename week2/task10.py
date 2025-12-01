import datetime
import os
# Using datetime, add a week and 12 hours to a date.  Given date: March 22, 2020, at 10:00 AM. print original date time and new date time
d = datetime.datetime(2016, 7, 24, 12, 30, 45, 10000)
tdelta = d + datetime.timedelta(weeks=1) + + datetime.timedelta(hours=12)
print(tdelta)


# Code to get the dates of yesterday, today, and tomorrow.
today = datetime.date.today()
yesterday = datetime.date.today() - datetime.timedelta(days=1)
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
print(yesterday)
print(today)
print(tomorrow)


# Write a code snippet using os module, to get the current working directory and print and create a folder “test”. List all the files and folders in the current working directory and remove the directory “test” that was created.
cwd = os.getcwd()
print("Current Working Directory:", cwd)

folder_name = "test"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f'Folder "{folder_name}" created.')
else:
    print(f'Folder "{folder_name}" already exists.')


print("Contents of the directory:")
for item in os.listdir(cwd):
    print(item)

if os.path.exists(folder_name):
    os.rmdir(folder_name)
    print(f'Folder "{folder_name}" removed.')


# Write a Python program to rename a file from old_name.txt to new_name.txt.
old_name = "old_name.txt"
new_name = "new_name.txt"

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f'File renamed from "{old_name}" to "{new_name}".')
else:
    print(f'File "{old_name}" does not exist.')



# Create a file and Write a Python program to get the size of a file named example.txt
file_name = "example.txt"
with open(file_name, "w") as f:
    f.write("This is an example file.")

print(f'"{file_name}" created and written successfully.')

if os.path.exists(file_name):
    size = os.path.getsize(file_name)
    print(f'Size of "{file_name}": {size} bytes')
else:
    print(f'File "{file_name}" does not exist.')


# Convert the string "Feb 25 2020 4:20PM" into a Python datetime object
# O/P: 2020-02-25 16:20:00
date_str = "Feb 25 2020 4:20PM"
dt = datetime.datetime.strptime(date_str, "%b %d %Y %I:%M%p")
print(dt)




# Subtract 7 days from the date 2025-02-25 and print the result.
# O/P: New date: 2025-02-18
d = datetime.date(2025, 2, 25,)
seven_days_before = d - datetime.timedelta(weeks=1)
print(seven_days_before)


# Format the date 2020-02-25 as "Tuesday 25 February 2020"
date_obj = datetime.datetime.strptime("2020-02-25", "%Y-%m-%d")
formatted = date_obj.strftime("%A %d %B %Y")
print(formatted)