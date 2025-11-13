#Logical Operators = evaluate multiple conditions (or, and, not)
#   or = at least one condition must be True
#   and = both conditions must True
#   not = inverts the conditions (not False, not True)

#OR
temp = 80
is_raining = True

if temp < 50 or temp < 0 or is_raining:         #this is an (OR) operator The if statement is true at least one condition is true
    print("The Outdoor event is cancelled")
else:
    print("The Outdoor event is still scheduled")
#AND + NOT
temp = 90
is_sunny = True

if temp >= 75 and is_sunny:                      #this is an (AND) operator The if statement is true both conditions are true
    print("Its Stupid hot ouside")
    print("Its Sunny Outside right now")
elif temp >= 50 and is_sunny:
    print("Its Ball weather")
    print("Its Sunny Outside right now")
elif 30 > temp > 0 and is_sunny:
    print("Its Cold as fuck outside")
    print("Its Sunny Outside right now")
elif temp >= 75 and not is_sunny:
    print("Its Stupid hot ouside")
    print("Its is Cloudy outside right now")
elif temp >= 50 and not is_sunny:
    print("Its Ball weather")
    print("Its is Cloudy outside right now")
elif 30 > temp > 0 and not is_sunny:
    print("Its Cold as fuck outside")
    print("Its is Cloudy outside right now")
else:
    print("You Good to Go out and play Ball")