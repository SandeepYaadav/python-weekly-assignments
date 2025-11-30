#1. Write a function that appends 1 to 1000 numbers to a list and add a decorator to that function to calculate the start and end time. Calculate the total time taken and print.
import time

from week2.task1 import my_floats


def add_start_and_end_time(func):
    def wrapper(*args, **kargs):
        start_time = time.time()
        func(*args, **kargs)
        end_time = time.time()
        print("Total Execution Time: ", end_time - start_time)
    return wrapper

@add_start_and_end_time
def append_numbers():
    num_list = []
    for x in range(1, 1001):
        num_list.append(x)
    return num_list

append_numbers()


# 2. Create a parameterised decorator retry that retries a function a specified number of times.
#
# 	@retry(3)
#             def may_fail(name):
#                   print(f"Hello, {name}!")
def retry(times):
    def decorator(func):
        def wrapper(*args, **kargs):
            for x in range(1, times+1):
                 func(*args, **kargs)
        return wrapper
    return decorator

@retry(4)
def may_fail(name):
    print(f"Hello, {name}!")

may_fail("sandeep")




# 3. Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.
#
#           def square_root(x):
#     		return x ** 0.5

def validate_positive(func):
    def wrapper(x,*args,**kargs):
        if x < 0:
            raise ValueError("Passed number must be a positive number!!")
        return func(x,*args, **kargs)
    return wrapper

@validate_positive
def square_root(x):
    return x ** 0.5

print(square_root(2))

# 4. Create a decorator cache that caches the result of a function based on its arguments.
# 	@cache
#       	def expensive_computation(x):
#     		print("Performing computation...")
#     		return x * x
#
# expensive_computation(5)
# expensive_computation(5)
# Write a cache decorator for it to check if the calculation is already performed then return the result.
def cache(func):
    cached_results = {}

    def wrapper(*args, **kwargs):
        # Create a key based on arguments
        key = args + tuple(sorted(kwargs.items()))
        if key in cached_results:
            print("Returning cached result...")
            return cached_results[key]
        else:
            result = func(*args, **kwargs)
            cached_results[key] = result
            return result

    return wrapper

@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x

expensive_computation(5)
expensive_computation(5)

# 5. Create a decorator requires_permission that checks if a user has the ‘admin’ permission before allowing access to a function, if a different user then responds “Access denied”.
#
#  	 def delete_user(user, user_id):
#     		print(f"User {user_id} deleted by {user['name']}")
#
# 	user1 = {'name': 'Alice', 'permissions': ['admin']}
# 	user2 = {'name': John, 'permissions': ['dev']}
# 	user3 = {'name': 'Kurt', 'permissions': ['test’']}

def requires_permission(func):
    def wrapper(user, *args, **kwargs):
        if "admin" in user.get("permissions", []):
            return func(user, *args, **kwargs)
        else:
            print("Access denied")
    return wrapper

@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")

user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test']}

delete_user(user1, 101)  # Allowed
delete_user(user2, 102)  # Denied
delete_user(user3, 103)  # Denied





