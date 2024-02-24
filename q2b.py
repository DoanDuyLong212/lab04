#1
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        words = text.split()
        total_words = len(words)
        print(f"The total number of words in the file '{file_path}' is: {total_words}")
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")

count_words_in_file(input('enter file name'))
#2
def display_words():
    try:
        with open('story.txt', 'r') as file:
            lines = file.readlines()
        words = [word for line in lines for word in line.split()]
        short_words = [word for word in words if len(word) < 4]
        print("Words less than 4 characters in length:")
        for word in short_words:
            print(word)
    except FileNotFoundError:
        print("The file 'story.txt' was not found.")
display_words()
