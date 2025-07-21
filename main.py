import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')
user_input = input("Enter a word: ").lower()
user_input = list(user_input)
new1_dict = []

phonetic_dict = {row.letter.lower(): row.code for (_, row) in df.iterrows()}

for letter in user_input:
    if letter in phonetic_dict:
        new1_dict.append(phonetic_dict[letter])

print(new1_dict)
