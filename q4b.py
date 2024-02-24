#1
def hash_display(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        hashed_text = "#".join(text)
        print(hashed_text)
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")

hash_display(input('enter file name: '))
#2
def JTOI(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        corrected_text = text.replace('J', 'I')
        print(corrected_text)
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")

JTOI('WORDS.TXT')