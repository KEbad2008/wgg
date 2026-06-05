# Username: @ebaduk117
# Date: 2026 June 4th.
# File: wgg.py (wordguessinggame)
# Desc: Word Guessing Game In Python 

# Import Section - 
import random
import time

# Input - ask user to choose an option to run a function.
master_list = ["happy", "hairbrush", "pencil", "pillow", "monkey", "television", "smile", "couch", "games", "turtle", "toothbrush", "glasses", "chair", "bathtub", "bench", "piano", "pizza", "notebook", "hallway", "breakfast", "book", "iphone", "samsung"]


def get_option():
    print("----------------Menu:----------------:")
    print("1 - Play The Game")
    print("2 - Game instructions")
    print("3 - Quit Game")


    user_options = input("Please choose a option [1], [2], [3]: ")
    print()

    while (user_options != "1") and (user_options != "2") and (user_options !=  "3"):
        print("You must choose a option from 1-3!")
        print()
        user_options = input("Please choose a option [1], [2], [3]: ")
    return user_options


def get_word(ml):
    word = random.choice(ml)
    return list(word)



# Process/Output

def display_instructions():
    print("*** Here are the instructions: ***")
    print("1 - Try to guess the secret word by guessing one letter at a time.")
    print("2 - If you get a letter correct, it will be revealed in the word.")
    print("3 - Otherwise, if your guess is incorrect, you will have up to 5 chances.")
    print("4 - If you guess all the letters correctly, within the 5 guess limit, you win.")
    print("5 - If you guess more than 5 letters incorrectly, you lose.")
    time.sleep(4)
    print()


# Word guessing game if user chooses to play.
def play_game():
    word = get_word(master_list)
    guessed = ["_"] * len(word)
    wrong_guesses = []
    incorrect_guesses = 0
    guesses_left = 5
    print("####### Welcome To The Word Guesser Game #######")
    print("The Word You Will Guess Has", len(word), "Letters.", "Good Luck!")
    print("You have 5 guesses that can be incorrect!")

    # Allow user to play if they didnt guess more then 5 times yet.

    while (incorrect_guesses < 5):
        print("Current Word:", end=" ")
        for letter in guessed:
            print(letter, end=" ")
        print()
        guess = input("Guess a letter: ")
        print()

        # check if user enter a proper value.
        while (len(guess) != 1) or not("a" <= guess <= "z"):
            print("Please Enter a Valid Single letter!")
            guess = input("Guess a Single Letter!: ")
            print()

        already_guessed = False

        if (guess in guessed) or (guess in wrong_guesses):
            already_guessed = True
        
        if already_guessed:
            print("you already guessed '", guess, "' Try Again! It wont be counted towoards your 5 guesses!")
            

        else:
            correct_guess = False
            for x in range(len(word)):
                if word[x] == guess:
                    guessed[x] = guess
                    correct_guess = True
            

            # output - tell user if they guessed answer wrong or right.
            if correct_guess:
                print("Good! that is a correct guess!")
                print("You have", guesses_left, "guesses left!")

            else:
                print("Nice try, but", guess, "is not in the word.")
                #print("you have", guesses_left, "guesses left!")
                if guess not in wrong_guesses:
                    wrong_guesses.append(guess)
                    incorrect_guesses += 1
                    guesses_left -= 1
                    print("You can be wrong", guesses_left, "more times!")

                else:
                    print("You have already guessed", guess, "incorrecttly! It wont count again.")

            # get the list version of the word as a string..
            word_string = ""
            for add_letter in word:
                word_string += str(add_letter)

        if "_" not in guessed:
            print("Good Job! You Guessed The Word! It was:", word_string)
            print()
            time.sleep(3)
            return 0
        
    if (incorrect_guesses == 5):
        print("You Lost! The word was:", word_string)
        print()



# ok, now based on what user enters, we need to run the correct function to either play the game, show instructions, or exit the program.
def main():
    play = True
    while play == True:
        user_options = get_option()
        if user_options == "1":
            play_game()
        elif user_options == "2": 
            display_instructions()
        elif user_options == "3":
            print("Thank You For Using The Word Guessing Game Program, Goodbye! :)")
            play = False


# Main program - call main() to Start program.
main()


