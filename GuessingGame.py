import random

n = random.randrange(1,99)
print("Here is a guessing game! \nTry to guess the number. It is a value from 1-100")
print("Enter your guess: ")
guess = int(input())
guesses = 1
while True:
    if guess < n:
        print ("Your guess is too low! ")
    if guess > n:
        print ("Your guess is too high! ")
    if guess == n:
        print ("Correct! ")
        break;
    print("Enter your guess: ")
    guesses += 1
    guess = int(input())

print("It took you " + str(guesses) + " guesses.")

n2= random.randrange(1,9)
print("Now try to guess a list of numbers! The range of numbers is 0-10.")
print("How many numbers do you want? ")
GUESSES = int(input())
numbers = []
actualNumbers = []
GuessesCounter = 0

while GuessesCounter < GUESSES:
    #get the usersers guesses
    print("Enter number " + str(GuessesCounter + 1))
    number = int(input())
    numbers.append(number)
    GuessesCounter += 1;

    #get the results
    actualNumbers.append(random.randrange(1,9))

correctCounter = 0

for i in range(0, len(numbers)):
    for x in range(0, len(actualNumbers)):
        if numbers[i] == actualNumbers[x]:
            correctCounter += 1



print("You got " + str(correctCounter) + " correct!")
print("Original: " + str(actualNumbers))
print("Your guess: " + str(numbers))

