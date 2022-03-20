import random


def welcome():
    name = input("Let's play Hangman! Choose a nickname: ").capitalize()
    if name.isalpha() == True:
        print(f"Hello, {name}, time for the good old game Hangman.")
    else:
        print("Enter your name using only letters")
        name = input("Enter the nickname here: ").capitalize()
        print(f"Hi, {name}, check the game's rules below.")


def play_again():
    response = input("Are you up to play again? yes/no. Enter 'Y' for YES or 'N' for NO").lower()
    if response == "y":
        game_run()
    else:
        print("It was fun isn't it? Hope to see you again!")


def get_word():
    # A function that generates the word which user is trying to guess
    words = ["Python", "beach", "cars", "computers", "hotels", "clubs"]
    return random.choice(words).lower()


def game_run():
    welcome()  # -> makes game running
    alphabet = ("abcdefghijklmnopqrstuv")
    word = get_word()  # -> this variable is set to the function for random word to be generated
    guessed_letters = []  # -> empty list for guessed letter
    tries = 7
    guessed = False
    print()  # -> prints empty line
    # is a guess hint for the player for number of letters contained in the word
    print("the word contains", len(word), "letters.")

    print(len(word) * '_')

    while guessed == False and tries > 0:
        print("You have " + str(tries) + " tries")
        guess = input("Guess a letter in the word or enter a full word.").lower()
        # player guess a letter
        if len(guess) == 1:
            if guess not in alphabet:
                print("Check again your letter. An alphabet is required not a number.")
            elif guess in guessed_letters:
                print("You already tried that letter. Guess another one!")
            elif guess not in word:
                print("That letter is not a part of the word.")
                guessed_letters.append(guess)
                tries -= 1
            elif guess in word:
                print("That letter is found in the word!")
                guessed_letters.append(guess)
            else:
                print("A wrong entry might be entered. Verify again your entry.")
        # -> letters that users choose and that are not equal to the number of letters in the word to guess
        else:
            print("Note that the length of your guess is not equal to the length of the correct word")
            tries -= 1

        status = ''
        if guessed == False:
            for letter in word:
                if letter in guessed_letters:
                    status += letter
                else:
                    status += '_'
            print(status)

        if status == word:
            print("Well done, the word is correct!")
            guessed = True
        elif tries == 0:
            print("Word is not guessed. You ran out of tries.")

    # -> In case player wants to continue -> play_again()
    play_again()


game_run()  # -> the program run