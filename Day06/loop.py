
# FOR LOOP: Print numbers and their squares
print("Squares of numbers from 1 to 5:")
for i in range(1, 6):
    print(f"{i} squared is {i*i}")

# FOR LOOP WITH LIST: Iterate through a list of fruits
fruits = ["apple", "banana", "kiwi", "mango"]
print("Fruits in the basket:")
for fruit in fruits:
    if fruit == "kiwi":
        continue  # skip kiwi
    print(fruit)

# NESTED LOOPS: Multiplication table
print("Multiplication table 1 to 3:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("-" * 10)