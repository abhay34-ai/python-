tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "Tea": {"Green": "Mild", "Black": "Strong"}
}

# Access "chai" dictionary
print(tea_shop["chai"])
# Output: {'Masala': 'Spicy', 'Ginger': 'Zesty'}

# Access "Masala" from inside "chai"
print(tea_shop["chai"]["Masala"])
# Output: Spicy

# Access "Tea" dictionary
print(tea_shop["Tea"])
# Output: {'Green': 'Mild', 'Black': 'Strong'}

# Access "Black" tea
print(tea_shop["Tea"]["Black"])
# Output: Strong



squared_nums={x:x**2 for x in range(0,10)}
print(squared_nums)

