import random

number = random.randint(1, 100)
print('I made up a number. Can you guess it?')
guess = 0
while guess != number:
    guess = int(input())
    if guess > number:
        print('Too high')
        continue
    elif guess < number:
        print('Too low')
        continue
    else:
        print('Congrats, you won!')

