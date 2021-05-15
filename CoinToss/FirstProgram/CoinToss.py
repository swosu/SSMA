import random

print("Hello, and welcome to our coin toss program.")

# Toss a single coin and see if it comes up heads or tails.

our_number = random.random()
print("Our first number is: ",our_number)

if our_number < 0.5 :
    print("Heads")
else:
    print("Tails")
        