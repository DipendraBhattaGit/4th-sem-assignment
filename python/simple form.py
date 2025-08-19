name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in feet: "))
country = input("Enter your country: ")

name_upper = name.upper()
nickname = (name_upper[:2] + name_upper[-2:])  # first two + last two letters

height_rounded = round(height, 2)

country_upper = country.upper()

print("\n--- User Information ---")
print(f"Hello {name_upper}")
print(f"You are {age} years old.")
print(f"Your height is {height_rounded:.2f} feet.")
print(f"You are from {country_upper}.")
print(f"Your nickname is {nickname}")
