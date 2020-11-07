from random import choice
count = 0
words = ["cat", "crocodile", "bear", "monkey", "mouse", "lion", "turtle", "rat", "racoon", "penguin", "kangaroo", "panda", "donkey", "hamster", "zebra", "elephant", "goat", "horse", "sheep", "deer", "giraffe", "koala", "leopard", "cheetah", "ostrich", "eagle", "spider", "tortoise", "shark", "whale", "chicken", "rhino", "marmot", "pig", "dolphin", "owl", "armadillo", "dog", "wolf", "cow", "skunk", "opossum", "camel", "alligator", "squirrel", "flamingo", "octopus", "squid", "snail", "hippopotamus", "yak"]
secret = choice(words)
# print(secret)
print("Try to guess my word. \n")
dashes = list("-" * len(secret))
print(" ".join(dashes))
while "-" in dashes:
	letter = str(input("Enter letter: "))
	if letter not in secret:
		print("Try again!")
		count = count + 1
	else:
		for i, el in enumerate(secret):
			if el == letter:
				dashes[i] = letter
				count = count + 1
		if dashes.count("-") == 0:
			print("".join(dashes))
		else:
			print(" ".join(dashes))
		count = count + 1
dashes = "".join(dashes)
print(f"You guessed the word it was {dashes}!")
print(f"You guessed it in {count} tries!")
again = str(input("Do you want to play again? "))
while again == "Yes":
	count = 0
	secret = choice(words)
	# print(secret)
	print("Try to guess my word. \n")
	dashes = list("-" * len(secret))
	print(" ".join(dashes))
	while "-" in dashes:
		letter = str(input("Enter letter: "))
		if letter not in secret:
			print("Try again!")
			count = count + 1
		else:
			for i, el in enumerate(secret):
				if el == letter:
					dashes[i] = letter
					count = count + 1
			if dashes.count("-") == 0:
				print("".join(dashes))
			else:
				print(" ".join(dashes))
			count = count + 1
	dashes = "".join(dashes)
	print(f"You guessed the word it was {dashes}!")
	print(f"You guessed it in {count} tries!")
	again = str(input("Do you want to play again? "))
else:
	print("Thank you for playing!")
