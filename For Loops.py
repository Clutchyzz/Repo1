# For Loops = execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.

credit_card = "1234-3232-3412-1324"

for x in range(1, 11, 2): # add reversed to reverse and after range we string indexing (start:end:step)
    print(x)

for x in (credit_card): # add reversed to reverse and after range we string indexing (start:end:step)
    print(x)

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)