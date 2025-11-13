#name = input("Enter your full name: ")
phone_number = input("Enter your Phone Number: ")
result = len(name) # Length/How many characters
result = name.find("G") # Find the occurance of a character and tells us many characters until that character
result = name.rfind("l") # same as find but in reverse So Find an Occurance counting backwards (-1:means cant find)
name = name.capitalize() # This will capitalize the letter of an string
name = name.upper() # This makes everything upper case
name = name.lower() # This makes everything lower case
result = name.isdigit() # This is a boolean that is True if its a digit(Even if there are letters and numbers(Gabe123):False)
result = name.isalpha() # This is a boolean that is True if all characters are characters of the alphabet(Even if there is a space it doesnt count(Gabriel Morales):False)
result = phone_number.count("-") # this counts whatver character  you input
phone_number = phone_number.replace("-", " ") # This replaces characters for characters(an empty string is to remove the first string from input)
If need help type in: print(help(str))

print(phone_number)









