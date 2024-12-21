import random

rand_num = random.randint(1, 100)

while True:
    try: 
        guess = int(input("Guess the number between 1 and 100: "))

        if guess < rand_num:
            print("\nToo low!\n")
        elif guess > rand_num:
            print("\nToo high!\n")
        else:
            print("\nCongratulations! You guessed the number.\n")
            break
    except ValueError:
        print("\nInvalid choice!\n")
       