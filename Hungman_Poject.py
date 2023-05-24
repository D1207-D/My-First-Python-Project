import random

print("Hello There !!! Welcome to Hangman")

word = ["car", "toy", "bank", "spoon", "watch", "fridge", "air", "water", "fire"]

secret_word = random.choice(word)

print("You Only get 5 Guesses")

display_word = []

for letter in secret_word:
    display_word += "_"
print(display_word)

num = 0
game_over = False
while not game_over:
    guess = input("Can you please guess a letter --> ").lower()

    for position in range(len(secret_word)):
        letter  = secret_word[position]
        if letter == guess:
            display_word[position]  = letter

    if guess not in secret_word:
        num +=1
        guesses_left = 5 - num
        print(f"You have only {guesses_left}Guesses Left!!!")
        if num >= 5:
            print("You lost")
            game_over = True
    print(display_word)

    if "_" not in display_word:
        print("You Win!!!!")
        game_over = True
