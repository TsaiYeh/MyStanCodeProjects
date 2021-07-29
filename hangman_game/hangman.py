"""
File: hangman_extension.py
Name: 吳采曄 Judy
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game.
    Users sees a dashed word, trying to correctly figure the un-dashed word out by inputting one character each round.
    If the user input is correct, show the updated word on console.
    Players have N_TURNS chances to try and win this game.
    """
    answer = random_word()                                  # Define answer as a string, returned from random_word().
    print('The word looks like: ', end='')
    for i in range(len(answer)):
        print('_', end='')                                  # Print the dashed word and the dash numbers equal to the length of the answer.
    print('')
    print('You have '+str(N_TURNS)+' guesses left.')
    guess = input('Your guess: ')                           # Define guess as input character from user.
    guess = guess.upper()                                   # Make the guess upper case to become case-insensitive.

    trial = 0                                               # Define trial as the times user guesses, starting from 0.
    ans = ''                                                # Define ans as an empty string of guess result.
    for i in range(len(answer)):
        ans += '_'                                          # ans starts with all dashes and the dash numbers equal to the length of the answer.

    while trial < N_TURNS:                                  # When user still have chances to guess.
        if not guess.isalpha() or len(guess) != 1:          # If the input is not alphabet or more than one alphabet,
            print('Illegal format.')                        # shows 'Illegal format' and ask for new input.

        elif guess not in answer:                           # If the input is alphabet but not in the answer
            trial += 1                                      # Guess time plus 1 for each wrong-answer input.
            print("There is no " + str(guess) + "'s in the word.")
            if N_TURNS - trial > 0:                         # If user hasn't spent all the guess times (lives)
                show_result(ans, trial)
            else:                                           # If user spends all his guess times (lives)
                print('You are completely hung :(')
                print('The word was: ' + str(answer))
                quit()                                      # End this program.

        else:                                               # If user guess correctly
            old_ans = ans                                   # Define old_ans as the value of ans from last round.
            ans = correct_guess(guess, answer)              # Define ans as the result of correct_guess function.
            ans = combine_result(ans, old_ans)              # Redefine ans as the result of combine_result function.
            print('You are correct!')
            if ans != answer:                               # If ans is not equal to answer
                show_result(ans, trial)
            else:                                           # If ans is totally the same as answer
                print('You win!!')
                print('The word was: ' + str(answer))
                quit()

        ans = ans                                           # Redefine guess result as the latest result.
        guess = input('Your guess: ')
        guess = guess.upper()


def correct_guess(guess, answer):
    """
    :param guess: str, input character from user.
    :param answer: str, returned from random_word().
    :return: str, showing which character(s) the user guesses correctly by making it un-dashed.
    Other characters remain as dashes.
    """
    long_guess = ''                                     # Define long_guess as an empty string.
    ans = ''
    for i in range(len(answer)):
        long_guess += guess                             # Fill long_guess with the character of guess, length equals to answer.
        if long_guess[i] == answer[i]:                  # If the character of such index in long_guess equals to the character of such index in answer
            ans += guess                                # Fill ans with guess
        else:                                           # If the characters are not the same
            ans += '_'                                  # Fill ans with dash
    return ans


def combine_result(ans, old_ans):
    """
    :param ans: str, the result of correct_guess function in this round.
    :param old_ans: str, the value of ans from last round.
    :return: combine the result of ans and old_ans to create a new string called new_ans,
    so all correctly-guessed characters can be shown in new_ans.
    """
    new_ans = ''                                        # Define new_ans as an empty string.
    for i in range(len(ans)):
        if ans[i].isalpha():                            # If the character of such index in ans is alphabet
            new_ans += ans[i]                           # Fill new_ans with the character from ans
        elif old_ans[i].isalpha():                      # If the character of such index in old_ans is alphabet
            new_ans += old_ans[i]                       # Fill new_ans with the character from old_ans
        else:                                           # If none are alphabet (meaning not guess correctly yet)
            new_ans += '_'                              # Remain dash
    return new_ans


def show_result(ans, trial):
    """
    :param ans: str, the result of correct_guess function in this round.
    :param trial: int, the times user guesses.
    :return: str, reminder to user the current guess status and how many lives left.
    """
    print('The word looks like: ' + str(ans))
    print('You have ' + str(N_TURNS - trial) + ' guesses left.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
