fruits = ["apple", "banana", "cherry","carrots","pinnapple"]
print(fruits)

print(fruits[0])
print(fruits[-1])

print(fruits[0:2])
print(fruits[:])
print(fruits[::2])

fruits.append("orange")
print(fruits)

fruits.insert(1, "mango")
print(fruits)


fruits[0]="kivi"
print(fruits)


# fruits[0:2]="kivi"
# print(fruits)

fruits[0:2]=["kivi"]
print(fruits)

fruits[2:4]=["RAMFAL","SITAFAL"]
print(fruits)










fruits.remove("banana")
print(fruits)

popped = fruits.pop()
print(popped)
print(fruits)

print(len(fruits))
print(fruits.count("apple"))
print(fruits.index("mango"))

fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

print(", ".join(fruits))




tea_varities = ['Black', 'green', 'Masala', 'White']

tea_varities[1:1] = ["test", "test"]
print(tea_varities)

print(tea_varities[1:2])

print(tea_varities[1:3])

tea_varities[1:3] = []
print(tea_varities)