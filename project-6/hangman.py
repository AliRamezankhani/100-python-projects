import random
from hangman_pic import hangman
from hangman_words import word_list

chosen_word = random.choice(word_list)
display = []
chosen_word_length = len(chosen_word)
lives = 6
for _ in range(chosen_word_length):
    display += "_"
print(display)
print(hangman[6])      
game_finished = False
while not game_finished:
    guess = input("Guess a letter: ").lower()
    for position in range(chosen_word_length):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]
    print(display)
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_finished = True
            print("You Lose.")
    if "_" not in display:
        game_finished = True
        print("Hoooray!!! You Win.")      
    print(hangman[lives])      
