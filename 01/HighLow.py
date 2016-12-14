import random

if __name__ == "__main__":
    number = random.randrange(0,100)
    found = False
    while not found:
        guess = int(input("Guess: "))
        if guess > number:
            print("Too High")
        elif guess < number:
            print("Too Low")
        else:
            print("Correct!")
            found = True
