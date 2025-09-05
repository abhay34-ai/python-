chai = "masala chai"
# immutable
# slicing
slice_chai1 = chai[0:6]   
slice_chai2 = chai[7:11]  
slice_chai3 = chai[-4:]   
slice_chai4 = chai[-11:-5] 
slice_chai5 = chai[0:11:2]  

print(slice_chai1)
print(slice_chai2)
print(slice_chai3)
print(slice_chai4)
print(slice_chai5)

# case stuff
print(chai.upper())
print(chai.lower())
print(chai.title())
print(chai.capitalize())

# remove extra space
print(chai.strip())

# find and replace
print(chai.replace("masala", "ginger"))
print(chai.find("chai"))
print(chai.startswith("masa"))
print(chai.endswith("chai"))
print("chai" in chai)

# working with lists
st1 = " Lemon,Ginger,Masala,mint"
print(st1.split(","))
print(st1.split())
print(st1.split("chai"))

st2 = "abhay"
print(st2.count("a"))
print(st2.index("h"))

# f-strings
chai_type = "masala"
quantity = 2
print(f"I want {quantity} cups of {chai_type} chai.")

# joining lists
chai_variaty = ["Lemon", "Masala", "Ginger", "Mint"]
print(", ".join(chai_variaty))
