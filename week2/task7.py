#1. Write a code using generator can be used to produce an infinite sequence of Fibonacci numbers
# Of 10  numbers
#
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()

for x in range(10):
    print(next(fib_gen))



# 2. Write a generator function called infinite_multiples(n) that yields multiples of the given base value indefinitely.
#
#   Input n=3
#
# Output:
# 3
# 6
# 9
# 12
# 15
#...
def multiply_3(n):
    a = 1
    while True:
        yield n * a
        a +=1

mul_3 = multiply_3(3)

for x in range(10):
    print(next(mul_3))





# 3. Write a generator function called repeat_word(word, times) that yields the given character char a specified number of times.
#
# word = “hello”
# times = 5

def repeat_word(word, times):
    for x in range(times):
        yield word

word_gen = repeat_word("hello", 5)

for w in word_gen:
    print(w)

