chai_type = {
    "Black": "Strong flavor",
    "Green": "Light and healthy",
    "Masala": "Spicy and aromatic",
    "White": "Mild flavor"
}

# Add a new key "green" (different from "Green")
chai_type["green"] = "Fresh"
print(chai_type)

# Loop through dictionary using keys
for chai in chai_type:
    print(chai, chai_type[chai])

# Loop through dictionary using items()
for key, value in chai_type.items():
    print(key, value)
    
if "Masala" in chai_type:
    print("I have masala chai")
    
# Create a new dictionary from a list of keys with default value None
keys = ["masala", "Ginger", "Lemon"]
new_dict = dict.fromkeys(keys, "Default value")
print(new_dict)
    
keys = ["masala", "Ginger", "Lemon"]
new_dict = dict.fromkeys(keys, "")
print(new_dict)


chai_type["red"]="bad in taste"
print(chai_type)

del chai_type["red"]
print(chai_type)
