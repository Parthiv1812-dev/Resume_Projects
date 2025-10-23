student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    print(key, value)
    pass

import pandas
from pandas import DataFrame
student_data_frame = DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# final_dict = {}
# for (index, rows) in data.iterrows():
#     final_dict[rows.letter] = rows.code

final_dict  = {rows.letter: rows.code for (index, rows) in data.iterrows()}


print(final_dict)





#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name  = input("Enter your name: ").upper()
try:
    code_list = [final_dict[letter] for letter in name]
except KeyError:
    print("Sorry, only letters in the alphabet please.")
    name = input("Enter your name: ").upper()
    while name.isnumeric():
        print("Sorry, only letters in the alphabet please.")
        name = input("Enter your name: ").upper()

    code_list = [final_dict[letter] for letter in name]
# for letter in name:
#     try:
#         code_list.append(final_dict[letter])
#     # code_list.append(final_dict.get(letter))
#     except KeyError:
#         error = True
#         while error:
#             print("Sorry, only letters in the alphabet please.")
#             name = input("Enter your name: ").upper()
#             if not name.isnumeric():
#                 error = False
#             for letter1 in name:
#                 code_list.append(final_dict[letter1])


print(code_list)

