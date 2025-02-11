from wonderwords import RandomWord
import random

def load_word_list(filename: str):
    # Returns a list from a file with a series of words
    words = []
    with open(filename, "r", encoding = "UTF-8") as file:
        for line in file:
            words.append(line.strip())
    return words

def generate_word(letter: str):
    # Returns a random word that begins with the letter passed in
    pass

def print_a_letter():
    # Generates the first starting letter
    first_letter: str = random.choice("abcdefghijklmnopqrstuvwxyz")
    print(f"Type a word starting with the letter {first_letter}")  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Load list of animals to memory
    animal_list = load_word_list("animals.txt")

    # Create a word generator from the list
    generator = RandomWord(animal = animal_list)

    # Pick a random first letter
    print_a_letter()

    # TODO: Get user input (we should pick if sentence case or lowercase)
    # user_input: str = input ("Your word: ")

    print(generator.word())
    #animal list generated from goodgoodgood.co




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
