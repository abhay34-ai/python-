from datetime import date

while True:
    birth_year = input("Enter your birth year (or 'exit' to quit): ")
    if birth_year.lower() == 'exit':
        break
    if not birth_year.isdigit():
        print("Invalid input, try again")
        continue

    birth_year = int(birth_year)
    current_year = date.today().year
    age = current_year - birth_year
    print(f"You are {age} years old")

    if age < 0:
        print("You entered a future year! Try again.")
        continue
    elif age < 13:
        print("Child")
    elif age < 20:
        print("Teen")
    elif age < 60:
        print("Adult")
    else:
        print("Senior")
    
    if age >= 100:
        print("Wow! You are a centenarian!")
        break
