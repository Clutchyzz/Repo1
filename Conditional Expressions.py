#Conditional Expression = A one-line shortcut for the if-else statement (ternary operator)
#   print or assign one of two values based on a condition
#   X if condition else Y

num = 5
a = 6
b = 7
age = 5
temperature = 55
user_role = "admin"

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Child"
weather = "Hot" if temperature > 68 else "Cold"
access_level = "Granted" if user_role == "admin" else "Not Permitted"

print(access_level)




