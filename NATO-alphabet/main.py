import pandas
file = pandas.read_csv("nato_phonetic_alphabet.csv")
    
phonetic_alphabet = {row.letter: row.code for (index, row) in file.iterrows()}

word = input("Digite uma palavra: ").upper()
result = [phonetic_alphabet[letter] for letter in word]


print(result)