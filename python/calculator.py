num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

num1 = int(float(num1))
num2 = int(float(num2))

print("\n--- Choose an Operation ---")
print("1. Sum (+)")
print("2. Difference (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Integer Division (//)")
print("7. Power (^)")

choice = input("Enter your choice (1-7): ")

print("\n--- Result ---")

if choice == "1":
    print(f"Sum = {num1 + num2}")
elif choice == "2":
    print(f"Difference = {num1 - num2}")
elif choice == "3":
    print(f"Multiplication = {num1 * num2}")
elif choice == "4":
    if num2 != 0:
        print(f"Division = {num1 / num2}")
    else:
        print("Error! Cannot divide by zero.")
elif choice == "5":
    if num2 != 0:
        print(f"Modulus = {num1 % num2}")
    else:
        print("Error! Cannot take modulus by zero.")
elif choice == "6":
    if num2 != 0:
        print(f"Integer Division = {num1 // num2}")
    else:
        print("Error! Cannot divide by zero.")
elif choice == "7":
    print(f"Power = {num1 ** num2}")
else:
    print("Invalid choice! Please enter a number between 1 and 7.")
