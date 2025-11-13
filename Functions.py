# Function = A Block of reusable code
#            place () after the function name invoke it

def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy Birthday to you!")
    print()

happy_birthday("Gabe", 21)
happy_birthday("Babe", 29)
happy_birthday("Stef", 34)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Clutchyzz", 49.99, "5/13")

#return = statement used to end a function
#         and send a result back to the caller

def add(x, y):
    z = x + y
    return z
def subtract(x, y):
    z = x - y
    return z
def multiply(x, y):
    z = x * y
    return z
def divide(x, y):
    z = x / y
    return z

print(add(3, 7))
print(subtract(6, 3))
print(multiply(5, 10))
print(divide(10, 5))

