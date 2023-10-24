import pandas

def get_word(my_dict, entry):
    my_word = entry.upper()
    my_list = [my_dict[letter] for letter in my_word]
    return  my_list

letter_data = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_dict = letter_data.set_index("letter")["code"].to_dict()


word = input("Enter a word: ")
word_list = get_word(letter_dict, word)
print(word_list)