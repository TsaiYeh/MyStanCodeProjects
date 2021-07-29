"""
File: boggle.py
Name: 吳采曄 Judy Wu
----------------------------------------
This program mimics the boggle game. When user inputs 4 lines of 4 separated letters,
the program makes it a 4*4 matrix and finds all the possible words which are linked from a chosen letter
to its neighboring letters. Each word needs to contain 4 or more letters.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
ROW = 4										# the width of the matrix
COL = 4										# the height of the matrix
WORD_LEN = 4								# only find words whose length >= WORD_LEN
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'     # Alphabet index


def main():
	"""
	This function asks an user to input 4 lines of 4 separated letters and makes it a 4*4 matrix.
	It'll find and show all the possible words which are linked from a chosen letter to its neighboring letters.
	Each word needs to contain 4 or more letters.
	"""
	####################
	letter_lst = []														# the list will contain the input letters
	for i in range(ROW):
		row = input(f'{i + 1} row of letters: ').lower().split()		# user input is case-insensitive
		if len(row) != ROW:												# if user input too many/less letters
			print('Illegal input')
			quit()
		else:
			letter_lst.append(row)										# add the letters to letter_lst

	start1 = time.time()												# calculate read dictionary time
	dictionary = read_dictionary(letter_lst)
	end1 = time.time()

	start = time.time()													# calculate find word (recursion) time
	find_word(letter_lst, dictionary)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your read dictionary: {end1 - start1} seconds.')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(letter_lst):
	"""
	:param letter_lst: the list containing all the input letters
	:return: This function reads file "dictionary.txt" stored in FILE and appends words in each line into a Python list
	"""
	dictionary = [set() for i in range(26)]								# define dictionary_lst as a list of 26 sets
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip().lower()									# remove \n and become case-insensitive
			count = 0  													# assign count as 0
			if len(line) >= WORD_LEN:									# only add words >= 4 alphabets
				for i in range(len(line)):
					for j in range(len(letter_lst)):
						if line[i] in letter_lst[j]:					# compare if each alphabet in line exists in letter_lst
							count += 1									# if exists, count plus 1
							break
				if count == len(line):									# if all alphabets exist in letter_lst
					dictionary[ALPHABET.find(line[0])].add(line)		# add the line in one of the set of dictionary_lst
	return dictionary


def find_word(letter_lst, dictionary):
	"""
	:param letter_lst: the list containing all the input letters
	:param dictionary: A list containing all the words, whose letters shown in letter_lst, from the dictionary.
	:return: all the found words from letter_lst and print the number of words
	"""
	ans_lst = []				# define ans_lst as list containing all the words, existing in dictionary, from letter_lst.
	for x in range(ROW):
		for y in range(COL):
			cur = [(x, y)]										# define cur as list storing letter's position (x, y)
			find_word_helper(letter_lst, x, y, cur, ans_lst, dictionary)
	print(f'There are {len(ans_lst)} words in total.')  		# print the number of words


def find_word_helper(letter_lst, x, y, cur, ans_lst, dictionary):
	"""
	:param letter_lst: the list containing all the input letters
	:param x: int, the x-axis (row) index of the letter's position
	:param y: int, the y-axis (column) index of the letter's position
	:param cur: A list storing each letter's position (x, y)
	:param ans_lst: A list containing all the words which exist in dictionary, from letter_lst. Empty in the beginning.
	:param dictionary: A list containing all the words, whose letters shown in letter_lst, from the dictionary.
	:return: update ans_lst with all the found words
	"""
	if len(cur) >= WORD_LEN:									# base case
		cur_str = ''  											# define cur_str as an empty string
		for i in range(len(cur)):  								# for each index in cur
			cur_str += letter_lst[cur[i][0]][cur[i][1]]  		# refer the index to the alphabet in letter_lst and add to cur_str
			# e.g. cur == [[0, 0], [0, 1], [0, 2], [0, 3]], add [f, y, c, l] into cur_str

		if has_prefix(cur_str[:2], dictionary):							# check if first 2 alphabets existing in dictionary
			if cur_str in dictionary[ALPHABET.find(cur_str[0])]:		# check if the word existing in dictionary
				if cur_str not in ans_lst:  							# if cur_str not yet in ans_lst
					ans_lst.append(cur_str)  							# add it into ans_lst
					print(f'Found "{cur_str}"')

		find_longer_word_helper(letter_lst, x, y, cur, ans_lst, dictionary)		# try to find longer words
		return ans_lst

	else:
		for i in range(x - 1, x + 2):  								# Check upper, same-row, and lower letter.
			for j in range(y - 1, y + 2):  							# Check left, same-column, and right letter.
				if 0 <= i < ROW and 0 <= j < COL:					# if i and j in range of matrix
					if (i, j) not in cur:
						# Choose
						cur.append((i, j))
						# Explore
						find_word_helper(letter_lst, i, j, cur, ans_lst, dictionary)
						# Un-choose
						cur.pop()


def find_longer_word_helper(letter_lst, x, y, cur, ans_lst, dictionary):
	"""
	:param letter_lst: the list containing all the input letters
	:param x: int, the x-axis (row) index of the letter's position
	:param y: int, the y-axis (column) index of the letter's position
	:param cur: A list storing each letter's position (x, y)
	:param ans_lst: A list containing all the words which exist in dictionary, from letter_lst. Empty in the beginning.
	:param dictionary: A list containing all the words, whose letters shown in letter_lst, from the dictionary.
	:return: update ans_lst with all the found words
	"""
	if len(cur) >= WORD_LEN + 1:									# base case for longer words
		cur_str = ''
		for i in range(len(cur)):
			cur_str += letter_lst[cur[i][0]][cur[i][1]]

		if has_prefix(cur_str[:2], dictionary):
			if cur_str in dictionary[ALPHABET.find(cur_str[0])]:
				if cur_str not in ans_lst:
					ans_lst.append(cur_str)
					print(f'Found "{cur_str}"')
		return ans_lst

	else:
		for i in range(x - 1, x + 2):
			for j in range(y - 1, y + 2):
				if 0 <= i < ROW and 0 <= j < COL:
					if (i, j) in cur:
						pass
					else:
						# Choose
						cur.append((i, j))
						# Explore
						find_longer_word_helper(letter_lst, i, j, cur, ans_lst, dictionary)
						# Un-choose
						cur.pop()


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary: (list) A list containing all the words, whose letters shown in letter_lst, from the dictionary.
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for ele in dictionary[ALPHABET.find(sub_s[0])]:
		if ele.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
