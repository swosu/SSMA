import random


def toss_coin():    # Toss a single coin and see if it comes up heads or tails.
    our_number = random.random()
    print(f'{our_number: .2f} means ', end='')

    if our_number < 0.5 :
        print("Heads")
        heads = True
    else:
        print("Tails")
        heads = False
    
    return heads
