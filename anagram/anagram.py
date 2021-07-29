"""
File: anagram.py
Name: 吳采曄 Judy Wu
----------------------------------
This program recursively finds all the anagram(s) for the word input by user and terminates when the
input string matches the EXIT constant defined at line 19.

If you correctly implement this program, you should see the number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                     # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'         # This is the filename of an English dictionary
EXIT = '-1'                     # Controls when to stop the loop
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'     # Alphabet index

# Global variable
dictionary = [set() for i in range(26)]


def main():
    """
    This program recursively finds all the anagram(s) for the word input by user and terminates when the
    input string matches the EXIT wording.
    """
    start = time.time()
    ####################
    read_dictionary()
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit) ')
    while True:
        s = input('Find anagrams for: ')                            # define user input as s.
        if s == EXIT:                                               # if s equals to EXIT wording, break the while loop.
            break
        else:
            print('Searching...')
            anagrams = find_anagrams(s)                             # find anagrams
            for anagram in anagrams:
                print(f'Found: {anagram}')                          # print each anagram
                print('Searching...')
            print(f'{len(anagrams)} anagrams: {anagrams}')          # print the number of anagrams and all anagrams
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    :return: dictionary_lst with all the dictionary words inside.
    """
    global dictionary                                           # global variable
    with open(FILE, 'r') as f:
        for line in f:
            dictionary[ALPHABET.find(line[0])].add(line.lower().strip())


def find_anagrams(s):
    """
    :param s: str, input from user
    :return: a list contains all the anagrams of s
    """
    s_lst = []                                                  # define s_lst as list containing all the index of s
    for i in range(len(s)):
        s_lst.append(i)

    # define full_lst as list containing all the variety of s. The variety may or may not exist in dictionary.
    full_lst = []
    find_anagrams_helper(s, s_lst, [], full_lst)

    # define anagrams as list containing all the anagrams of s. The anagrams all exist in dictionary.
    anagrams = []
    for result in full_lst:
        if has_prefix(result[: 1]):                             # if prefix of the variety exists in dictionary
            if has_prefix(result[: 3]):
                if result in dictionary:                    # if the whole variety exists in dictionary
                    anagrams.append(result)                     # add it into anagrams list
    return anagrams


def find_anagrams_helper(s, s_lst, current_s, full_lst):
    """
    :param s: str, input from user
    :param s_lst: list, containing all the index of s
    :param current_s: an empty list, will add the index from s_lst to current s recursively
    :param full_lst: an empty list
    :return: full_lst with all the variety of s. The variety may or may not exist in dictionary.
    """
    if len(current_s) == len(s):                        # base case is length of current_s equals to length of s
        current_string = ''                             # define current_string as an empty str
        for ele in current_s:                           # for each ele in current_s
            current_string += s[ele]                    # refer the index to the alphabet in s and add to current_string
        if current_string not in full_lst:              # if current_string not yet exists in full_lst
            full_lst.append(current_string)             # add it into full_lst
        return full_lst
    else:                                               # recursion
        for ele in s_lst:
            if ele in current_s:                        # if ele already in current_s, do not add it again
                pass
            else:
                # Choose
                current_s.append(ele)
                # Explore
                find_anagrams_helper(s, s_lst, current_s, full_lst)
                # Un-choose
                current_s.pop()


def has_prefix(sub_s):
    """
    :param sub_s: str, prefix of s
    :return: boolean, return True if prefix in dictionary
    """
    for words in dictionary[ALPHABET.find(sub_s[0])]:
        if words.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
