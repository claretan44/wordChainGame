from wonderwords import RandomWord
import random
import string

class WordGame:

    def __init__(self, word_file):
        self.used_player_words = []
        self.used_pc_words = []
        self.curr_player_word = ""
        self.curr_pc_word = ""
        self.valid_words = {}
        self.curr_letter = random.choice(string.ascii_lowercase)

        self.load_word_list(word_file)

    def load_word_list(self, filename: str):
        # Loads the list of words

        index = 0
        with open(filename, "r", encoding="UTF-8") as file:
            for line in file:
                line = line.strip()
                if line.isalpha() and line[0] in string.ascii_lowercase:
                    while line[0] != string.ascii_lowercase[index] :
                        index += 1

                    if string.ascii_lowercase[index] not in self.valid_words:
                        self.valid_words[string.ascii_lowercase[index]] = []

                    self.valid_words[string.ascii_lowercase[index]].append(line)

    def try_set_pc_word(self):
        # There wasn't even a word with that letter in the file
        if self.curr_letter not in self.valid_words:
            return False

        # List is empty, all words used
        if not self.valid_words[self.curr_letter]:
            return False

        # There should be at least one word possible, generate now
        self.curr_pc_word = random.choice(self.valid_words[self.curr_letter])

        self.used_pc_words.append(self.curr_pc_word)

        # Remove from valid words dictionary
        self.valid_words[self.curr_letter].remove(self.curr_pc_word)
        # Set the current letter to the last letter of the pc word
        self.curr_letter = self.curr_pc_word[-1]

        return True

    def valid_player_word(self):
        # Check that the word has the right first letter
        if not self.curr_letter == self.curr_player_word[0].lower():
            return False

        if self.curr_player_word.lower() in self.valid_words[self.curr_letter]:
            # Player word is valid
            self.register_player_word()
            return True

        else:
            return False

    def register_player_word(self):
        self.used_player_words.append(self.curr_player_word.lower())

        # Remove from valid words dictionary
        self.valid_words[self.curr_letter].remove(self.curr_player_word.lower())
        self.curr_letter = self.curr_player_word.lower()[-1]
