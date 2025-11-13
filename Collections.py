# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ("apple", "orange", "banana", "coconut")
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple" in fruits)
#   LIST:
fruits[0] = "pineapple"
fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0, "apple")
fruits.sort()
fruits.reverse()
print(fruits.index("apple"))
#   SET:
fruits.remove("apple")
fruits.clear()
#   Tuple:
fruits.index("apple")

print(fruits)
for fruits in fruits:
    print(fruits)