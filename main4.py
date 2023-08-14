import pandas

data = pandas.read.csv("nato_pheotic_alphabet.csv")
print(data.to_dict())
# {new_key:new_value for (index, row) in df.iterrow()}
#TODO 1. Create a dictionary in this format
pheotic_dict = {row.letter:row.code for (index, row) in df.iterrow()}
# print(pheotic_dict)

#TODO 2. Create a list of the pheotic code words from a word that the user inputs.
words = input("Enter a word").upper()
output_list = [pheotic_dict[letter] for letter in word]
print(output_list)

