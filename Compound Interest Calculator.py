# Interest = the cost of borrowing money or the return for saving/investing it, charged as
# a percentage of the principal amount. When you borrow, interest is the extra money
# you pay back to the lender. When you save or invest, it's the money you earn from the
# bank or financial institution on your deposits or investments.

principle =  0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("principle cant be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate cant be less than zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time cant be less than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s: ${total:.2f}")