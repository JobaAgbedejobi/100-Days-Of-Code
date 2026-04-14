student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alpha", "B": "Bravo"}

phonetic_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
p_a = pd.DataFrame(phonetic_alphabet)

phonetic_dict = {row.letter: row.code for (index, row) in p_a.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#input("Enter a word:")

#word = input("Enter a word: ").upper()
# coded_phrase = [phonetic_dict[letter] for letter in word if letter in phonetic_dict]
# print(coded_phrase)


#DAY-30: EXCEPTION HANDLING
def generate_word():
    try:
        word = input("Enter a word: ").upper()
        coded_phrase = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("Sorry, only letters in the alphabet are allowed")
        generate_word()

    else:
        print(coded_phrase)

generate_word()