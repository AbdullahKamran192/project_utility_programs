import re

num_to_letter = {
    "0" : "O",
    "1" : "I",
    "2" : "Z",
    "5" : "S",
    "8" : "B",
    "6" : "G"
}

uppercase_letters_to_numbers = {
    "O": "0",
    "I" : "1",
    "Z": "2",
    "S" : "5",
    "B" : "8",
    "G" : "6"
}

def check_current_style_standard_plate(plate_text):

    new_plate_text = ""

    if re.match(r'^[A-Z0-9]{4} [A-Z0-9]{3}$', plate_text):
        print("Match")
        print(plate_text[0:5])

        part1 = plate_text[0:2] #2 letters
        part2 = plate_text[2:4] #2 numbers
        part3 = plate_text[4] # one blank space
        part4 = plate_text[5:8] #3 letters

        for i in range(len(part1)):
            if plate_text[i].isnumeric():
                new_plate_text += change_numbers_to_letters(plate_text[i])           

        print(f"The plate is {new_plate_text}")

    else:
        print("This is a custom plate, not a standard UK plate.")
    

def change_letters_to_num(letter):
    number = uppercase_letters_to_numbers.get(letter)

    if number is not None:
        return number
        

def change_numbers_to_letters(number):
    letter = num_to_letter.get(number)

    if letter is not None:
        return letter

    return number

check_current_style_standard_plate("29OI 0ZX")