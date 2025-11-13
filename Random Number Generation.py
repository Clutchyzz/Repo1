import random

low = 1
high = 100
options = ("rock", "paper", "Scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# print(help(random))
number = random.randint(low, high) # random.rand = random rand int = random number/integer
number = random.random() # This gives a random float under 1
option = random.choice(options)
random.shuffle(cards)
print(cards)