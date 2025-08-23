def make_card(name, age, message="Take care of your health."):
    return f"Hello {name} ({age} years old)!\n{message}"

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
print(make_card(user_name, user_age))