import wordgame


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Load list of animals to memory
    try:
        game = wordgame.WordGame("animals.txt")
    except FileNotFoundError:
        # Something went wrong with the file
        print("Error: Could not load word database")
    else:
        while True:
            user_input: str = input (f"Enter an animal that starts with the letter {game.curr_letter}: ")

            game.curr_player_word = user_input
            if not game.valid_player_word():
                print("You lose!")
                print("Your chained words: ")
                for word in game.used_player_words:
                    print(word)
                print (f"Your total score: {len(game.used_player_words)}")
                break
            else:
                if not game.try_set_pc_word():
                    print("The Ai couldn't come up with a word, you win!")
                    print("Your chained words: ")
                    for word in game.used_player_words:
                        print(word)
                    print(f"Your total score: {len(game.used_player_words)}")
                    break
                else:
                    print(f"The AI's word is {game.curr_pc_word}")


    #animal list generated from goodgoodgood.co





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
