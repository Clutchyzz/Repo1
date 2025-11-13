# Nested Loop = A loop within another loop (outer, inner)
#   outer loop:
#       inner loop:
rows = int(input("Enter the # of rows: "))
Columns = int(input("Enter the # of Columns: "))
symbol = input("Enter a symbol to use: ")





for x in range(rows):
    for y in range(Columns):
        print(symbol, end=" ") # the "" is i what the spacing is
    print()