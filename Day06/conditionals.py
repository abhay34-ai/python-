age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
elif age < 60:
    print("Adult")
else:
    print("Senior")


if age < 12:
    print("Child ticket: 50% off")
elif age >= 60:
    print("Senior citizen ticket: 30% off")
else:
    print("Regular price ticket")

age = int(input("Enter your age: "))
if age < 18:
    print("Suggested: Light exercise")
elif age <= 40:
    print("Suggested: Moderate exercise")
else:
    print("Suggested: Low-impact exercise")
