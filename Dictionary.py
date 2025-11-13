# Dictionary = A Collection of {key:Value} pairs
#              ordered and changeable. NO Duplicates

capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Beijin",
            "Russia": "Moscow"}
             # keys    # Values
 print(capitals.get("Oklhoma"))
if capitals.get("New Jersey"):
    print("This Capital Exist")
else:
    print("This Capital doesnt exist")

 capitals.update({"Germany": "Berlin"})
 capitals.update({"USA": "Detroit"})
 capitals.pop("USA") # This removes
 capitals.popitem # This removes the lastest item added
 capitals.clear()

keys = capitals.keys()
for key in keys:
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}:{value}")

