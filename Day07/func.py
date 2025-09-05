# SIMPLE FUNCTION
def greet(name):
    return f"Hello, {name}!"

print(greet("Abhay"))

# LAMBDA FUNCTION
square = lambda x: x * x
print(f"Square of 5: {square(5)}")

# GENERATOR FUNCTION
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

print("Even numbers up to 10:")
for num in even_numbers(10):
    print(num, end=" ")
print()

# FUNCTION WITH *ARGS
def add_numbers(*args):
    return sum(args)

print(f"Sum: {add_numbers(5, 10, 15)}")

# FUNCTION WITH **KWARGS
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Abhay", age=20, city="Nagpur")
