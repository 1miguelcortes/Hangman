import re

def main():
	debug = True
	incorrectGuesses = 0
	guessedLetters = []

	alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

	wordsFile = open("words_alpha.txt","r")
	wordsFiltered = wordsFile.read().split("\n")
	
	print("Enter your phrase with letters represented by underscores")
	print("For example enter 'Ubuntu Linux' as ______ _____")
	print("When asked for a position, give the positions in the phrase, with the first charicter being 1 excluding spaces")
	print("In the above exaple, if the letter being guessed is 'u' enter '4 9")
	print("If a guess is incorrect, enter n or N")
	working_guess = input("Phrase: ").replace('_','.')

	solved = False
	while not solved:
		#Generate a wordlist
		temp_wordlist = []
		wordPatterns = working_guess.split(' ')
		for x in range(0, len(wordPatterns)):
			wordPatterns[x] = re.compile(wordPatterns[x])
		for x in range(0, len(wordsFiltered)):
			matched = False
			y = 0
			while not matched:
				if wordPatterns[y].match(wordsFiltered[x]):
					temp_wordlist.append(wordsFiltered[x])
					matched = True
				else:
					pass
				y = y + 1
		wordsFiltered = temp_wordlist
		#Generate letter probabilities
		letterProbabilities = {}
		for x in range(0,len(alpha)):
			total = 0
			for y in range(0,len(wordsFiltered)):
				if alpha[x] in wordsFiltered[y]:
					total = total + 1
			letterProbabilities[alpha[x]] = total / len(wordsFiltered)
		for x in range(0, len(guessedLetters)):
			letterProbabilities[guessedLetters[x]] = 0

		#Replace wildcards with letters if correct, otherwise skip
		guess = list(letterProbabilities.keys())[list(letterProbabilities.values()).index(max(letterProbabilities.values()))]
		pos = input("Does your phrase contain the letter " + guess + "? (Numbers or N)")
		if pos.upper() == 'N':
			incorrectGuesses = incorrectGuesses + 1
		else:
			working_guess = list(working_guess)
			pos = pos.split(' ')
			for x in range(0,len(pos)):
				working_guess[int(pos[x])-1] = guess
			working_guess = ''.join(working_guess)
		guessedLetters.append(guess)
		#Check if solved
		print("incorrect Guesses: " + str(incorrectGuesses))
		print("Your phrase so far: " + working_guess.replace('.','_'))
		if incorrectGuesses >= 6:
			print("6 incorect guesses reached, you win")
			exit()
		else:
			pass
		if '.' not in working_guess:
			print("Your phrase has been guessed, computer wins")
			solved = True
	exit()

if __name__ == '__main__':
    main()