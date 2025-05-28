import random
import math
word_list = ["camel", "baboon", "aardvark"]

random_number = math.floor(random.random() * len(word_list))


randomly_chosen_word = word_list[random_number]
total_value = 0
for i in range(0, len(randomly_chosen_word)):
    total_value += i


wrong_guesses = 7
correct_guesses = []

print(len(randomly_chosen_word))



def guess_or_not (my_list, index):
    for guess in my_list:
        if guess == index:
            return True
    return False


user_win = False
while wrong_guesses > 0:
    correct_guess = False
    user_guess = input("What is your letter guess (make sure it is in lowercase): ")
    index = 0
    for letter in randomly_chosen_word :
        if letter == user_guess:
            if not guess_or_not(correct_guesses, index):
                correct_guesses.append(index)
                index += 1
                correct_guess =True
                print(f"You have guessed correctly. The correct guess is: {user_guess}")
                break
        index += 1
        
    # check if user completed the game (guessed correctly all the letters of the word)
    if len(correct_guesses) == len(randomly_chosen_word):
        user_win = True
        break

    if not correct_guess :
        wrong_guesses -= 1
        print(f"The user has guessed incorrectly. The incorrect guess: {user_guess}")
    
if user_win:
    print("The user have won")
else:
    print("The user have lost.")



