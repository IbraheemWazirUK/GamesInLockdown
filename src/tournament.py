import random
from enum import Enum

class T_Tournament(Enum):
	LEAGUE = 1
	ELIMINATION = 2
	BRACKET = 3

class Tournament:
	def __init__(self, name)
		self.name = name

class Bracket(Tournament):

	def __init__(self, name, no_of_players, players_per_game):
		super(name)
		self.players_per_game = players_per_game
		self.no_of_players = no_of_players
		self.left_spaces = [i for i in range(no_of_players)]
		n = no_of_players
		self.brackets = []
		while n > 0:
			n // = no_of_players
			self.brackets.append([["" for i in range(players_per_game)] for j in range(n)])

	def add_player(self, name):
		i = random.randint(len(left_spaces))
		space = left_spaces[i]
		del left_spaces[i]
		bracket_pos = space // players_per_game
		pos_in_bracket = space % players_per_game
		self.brackets[0][bracket_pos][pos_in_bracket] = name

	def record_win(self, bracket_no, bracket_pos, name):
		if bracket_no < len(self.brackets) - 1:
			self.brackets[bracket_no+1][bracket_pos//players_per_game][bracket_pos%players_per_game] = name



class Elimination(Tournament):
	def __init__(self, name, no_of_eliminations):
		super(name)
		self.no_of_eliminations = no_of_eliminations
		self.players = []

	def add_player(self, name):
		self.players.append(name)

	def eliminate(self, eliminations):
		for player in eliminations:
			self.players.remove(player)

class League(Tournament):
	def __init__(self, name, no_of_players, points_for_win = 1, points_for_draw = 0, points_for_loss = 0):
		super(name, no_of_players)
		self.points_for_loss = points_for_loss
		self.points_for_win = points_for_win
		self.points_for_draw = points_for_draw
		self.players = []
		self.table = {}
		self.matches = []

	def add_player(self, name):
		self.table[name] = [0, 0, 0, 0]
		players_copy = list(self.players)
		for i in range(len(self.players)):
			j = random.randint(len(players_copy))
			self.matches.append((name, players_copy[j]))
			del players_copy[j]

		self.players.append(name)

	def record_win(self, winner, loser):
		self.table[winner][0] += 1
		self.table[winner][3] += points_for_win
		self.table[loser][2] += 1
		self.table[loser][3] += points_for_loss

	def record_draw(self, name1, name2):
		self.table[name1][1] += 1
		self.table[name1][3] += points_for_draw
		self.table[name2][1] += 1
		self.table[name2][3] += points_for_draw

	def get_next_match(self):
		i = random.randint(len(self.matches))
		match = self.matches[i]
		del self.matches[i]
		return match

