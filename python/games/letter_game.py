import random

#make a list words
words=[
'apple',
'apricot',
'avocado',
'banana',
'bilberry',
'blackberry',
'blackcurrant',
'blueberry',
'boysenberry',
'currant',
'cherry',
'cherimoya',
'cloudberry',
'coconut',
'cranberry',
'cucumber',
'guava',
'honeyberry',
'huckleberry',
'jabuticaba',
'jackfruit',
'jambul',
'jujube',
'kiwifruit',
'kumquat',
'lemon',
'lime',
'loquat',
'longan',
'lychee',
'mango',
'rambutan',
'redcurrant',
'salak',
'satsuma',
'starfruit',
'strawberry',
'tamarillo',
'tamarind',
'tomato'
]

def game():

	# draw guesses and strikes
	# print/display win/lose

	while True:
		# pick up a random word
		word = random.choice(words)

		# draw spaces
		sword = word

		# display to the console the spaced word

		# take guessess
		guess = input("Input your guess: ")



game()
