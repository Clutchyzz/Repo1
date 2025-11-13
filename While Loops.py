# While Loop = execute code while some condition remains true
name = input("Enter your name: ")

while name == "":
    print("you did not enter your name")
    ame = input("Enter your name: ") # Always add a exist or you will get stuck in the while loop
print(f"Hello {name}!!")

age = int(input("Enter you age: "))

while age < 0:
    print("Age cant be negative")
    age = int(input("Enter you age: "))

print(f"You are {age} years old")

food = input("Whats a food you like?(Q to quit): ")

while not food == "q":
    print(f"You like {food}!")
    food = input("Whats another food you like?(Q to quit): ")
print("Bye")

num = int(input("Enter a # between 1 - 10: "))

while not num > 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))
print(f"Your Number is {num}")
print("Thanks for playing")