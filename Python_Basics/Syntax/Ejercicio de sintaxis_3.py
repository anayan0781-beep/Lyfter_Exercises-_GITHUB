import random

secret_number = random.randint(1, 10)

guess = int(input("Guess the secret number from 1 to 10: "))

while guess != secret_number:
    print("Wrong guess. Try again!")
    guess = int(input("Guess the secret number from 1 to 10: "))

print("Congratulations! You guessed the secret number!")

