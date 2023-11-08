import pandas
def check_input(my_dict):
    my_list = []
    word = input("Enter a word: ").upper()
    try:
        my_list = [my_dict[letter] for letter in word]
    except KeyError:
        correct = False
        while not correct:
            print("Only letters can be accepted. Try again.")
            word = input("Enter a word: ").upper()
            if word.isalpha():
                correct = True
                my_list = [my_dict[letter] for letter in word]
    return  my_list

letter_data = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_dict = letter_data.set_index("letter")["code"].to_dict()

word_list = check_input(letter_dict)
print(word_list)