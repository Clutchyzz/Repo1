# Indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

credit_number = "1234-1234-1234-1234"

print(credit_number[0])
print(credit_number[0:4])
print(credit_number[5:9])
credit_number[5:] # Python will assume [8:] means 8th all the way to the end and vice versa
print(credit_number[-1]) # -1 means last character
print(credit_number[::2]) # This will print every step number in the string this counts every 2 digits here

last_digits = credit_number[-4:] 
credit_number = credit_number[::-1] # this makes the characters/digits flip backwords
print(credit_number)