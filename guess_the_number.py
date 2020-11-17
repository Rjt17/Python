import random

guesses = 0
number = random.randint(1,50)

name = input("What is your name? ")

print(name + ", I am thinking of a whole number between 1 and 50. Can you guess what it is?\n")

while guesses < 10:
  guess = input("Take a guess \n")
  guess = int(guess)

  guesses = guesses + 1;
  guessesLeft = 10 - guesses;

  if guess < number:
    guessesLeft=str(guessesLeft)
    print("Your guess is too low! You have {} guesses left".format(guessesLeft))

  if guess > number:
    guessesLeft=str(guessesLeft)
    print("Your guess is too high! You have {} guesses left".format(guessesLeft))

  if guess==number:
    break

if guess==number:
  guesses=str(guesses)
  print("Good job! You guessed the number in  {} tries :)".format(guesses))

if guess!=number:
  number=str(number)
  print("Sorry. The number I was thinking of was {} :)".format(number))