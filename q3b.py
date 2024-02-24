#1
def count_uppercase_chars_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        uppercase_chars = [char for char in text if char.isupper()]
        total_uppercase_chars = len(uppercase_chars)
        print(f"The total number of upper characters in the file '{file_path}' is: {total_uppercase_chars}")
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")

count_uppercase_chars_in_file(input('enter file name: '))
#2
def count_this_and_these_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        words = text.split()
        count_this = words.count('this')
        count_these = words.count('these')
        print(f"The word 'this' appears {count_this} times in the file '{file_path}'")
        print(f"The word 'these' appears {count_these} times in the file '{file_path}'")
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        
count_this_and_these_in_file('article.txt')