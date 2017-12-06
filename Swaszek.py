""" 
Implementation of Swaszek's algorithm
for a game of Mastermind
with 4 positions and 6 colors.

Input: Master Code for algorithm to find.
Output: Code that algorithm guesses as Master Code 
		and number of turns it took to guess it.

Authors: Brenna Manning, Emma Price, and Rachel Yang
"""

import copy
import random

def all_possible_codes():
	""" Calculates and returns list of 
		all possible codes that codemaker 
		could choose. List should have 1296
		(6^4) codes. """ 
	all_codes = []

	# iterate through 6 colors for 4 positions
	for i in range(0,6):
		for j in range(0,6):
			for k in range(0,6):
				for l in range(0,6):
					all_codes.append([i,j,k,l])

	# error check
	if len(all_codes) == 1296:
		return all_codes
	else:
		print "Not all possible" + \
		" codes were correctly calculated," + \
		" %d codes found" % (len(all_codes))

def find_candidates(prev_candidates, curr_code, resp):
	""" Creates and returns new list of 
		possible candidates given 
		codemaker's response. """
	new_candidates = []
	black_candidates = []

	# find valid candidates using black pegs
	for candidate in prev_candidates:
		black_counter = 0
		for i in range(0,4):
			if candidate[i] == curr_code[i]:
				black_counter += 1
		if black_counter == resp[0]:
			black_candidates.append(candidate)

	# for the candidates that passed black pegs,
	# find valid candidates using white pegs 
	for candidate in black_candidates:
		white_counter = 0
		curr_code_copy = copy.deepcopy(curr_code)
		candidate_copy = copy.deepcopy(candidate)
		for i in range(len(curr_code_copy)):
			for j in range(len(candidate_copy)):
				if curr_code_copy[i] == candidate_copy[j]:
					curr_code_copy[i] = -1
					candidate_copy[j] = -1
					white_counter += 1
		# only pass when white counter adjusts for black pegs
		if white_counter == (resp[0]+resp[1]):
			new_candidates.append(candidate)
	return new_candidates

def play_turn(candidates, game_mode):
	""" Two game modes: random (r) or counting (c).
		If random, choose random candidate to play as move.
		If counting, choose first candidate in candidate space to play as move. 
		Returns next move using above. """

	if game_mode == "r":
		return candidates[random.randrange(0,len(candidates))]
	elif game_mode == 'c':
		return candidates[0]
	else:
		print "ERROR: not a game mode"

def get_response(code, master_code):
	""" Gets codemaker's response to guessed 
		candidate. Returns list of number of 
		black pegs and number of white pegs. """
	black_pegs = 0
	white_pegs = 0
	
	# find num of white pegs
	curr_code_copy = copy.deepcopy(code)
	master_copy = copy.deepcopy(master_code)
	for i in range(len(curr_code_copy)):
		for j in range(len(master_copy)):
			if curr_code_copy[i] == master_copy[j]:
				curr_code_copy[i] = -1
				master_copy[j] = -1
				white_pegs += 1

	# find num of black pegs
	for i in range(0,4):
			if master_code[i] == code[i]:
				black_pegs += 1

	# adjust white pegs
	white_pegs = white_pegs - black_pegs

	return (black_pegs, white_pegs)

def play_game(master_code, game_mode):
	""" Plays Mastermind. """
	candidates = all_possible_codes()
	num_turns = 0
	resp = (0,0)
	move = [1,1,2,2] 	# best first guess from background research
	while resp != (4,0) and (len(candidates) > 0):
		resp = get_response(move, master_code)
		candidates = find_candidates(candidates, move, resp)
		move = play_turn(candidates, game_mode)
		num_turns += 1
		print "move: " + str(move) + ". resp: " + str(resp)
	print "The game is over! The code is " + str(move) + ".The computer solved it in " + str(num_turns) + " turns."

play_game([1,1,1,1], 'r')