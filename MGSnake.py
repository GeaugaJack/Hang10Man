import random


def welcomescreen():
    name = input("Enter Your Name: ")
    print("Welcome", name, "to hangman!")
    print("try and guess the word in 10 tries or less")
    hangman()
    print()

def hangman():
    word = random.choice(["elephant", "giraffe", "spider", "fox", "platypus", "eagle", "kangaroo", "bobcat", "moose", "seahorse"])

    validletters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    turns = 10
    guessed = " "

    while len(word) > 0:
        msg = ""
        missed = 0
        for letter in word:
            if letter in guessed:
                msg = msg + letter
            else:
                msg = msg + "_" + " "
                missed += 1
        
        if msg == word:
            print(msg)
            print("You are correct, the word was: ", word)
            break

        print("Guess The Word:", msg)

        guess = input ()

        if guess in validletters:
            guessed = guessed + guess
        else:
            print("Enter a valid letter: ")

            guess = input()
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("  o")
            if turns == 8:
                print("  o")
                print("  |")
            if turns == 7:
                print("  o")
                print("  |")
                print("   \ ")
            if turns == 6:
                print("  o")
                print("  |")
                print(" / ")
            if turns == 5:
                print("  o")
                print("  |")
                print(" / \ ")
            if turns == 4:
                print("   o")
                print("   |")
                print(" _/ \_ ")
            if turns == 3:
                print("   o")
                print("   |-")
                print(" _/ \_ ")
            if turns == 2:
                print("   o")
                print("  -|-")
                print(" _/ \_ ")
            if turns == 1:
                print("You have failed to guess the word:", word)
                break

welcomescreen()