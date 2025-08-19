import random

# Final Challenge: Write a program where the user has to guess a secret number between 1 and 10. The program should provide 
# feedback if the guess is too high or too low and congratulate the user if they guess correctly.
# Randomly select a secret number between 1-10.
# Ask the user to make a guess between 1-10.
# If the user is correct, print "Congratulations, You guessed the secret number!"
# If the user is too low, print "Too low!"
# If the user is too high, print "Too high!"
guess_number = int(input("Guess a Number between 1 and 10"))


secret_number = random.randint(1, 10)

if guess_number == secret_number:
    print("Congratulations")
elif secret_number < guess_number:
    print("Too high!")
elif secret_number > guess_number:
    print("Too Low!")

else:
    print("Try again!")