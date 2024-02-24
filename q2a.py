#1
content = input("Enter some content to write to the file: ")
with open("myfile.txt", "w") as f:
    f.write(content)
    
#2    
file_name = input("Enter the file name: ")
with open(file_name, 'w') as file:
    text = input("Enter the text to write to the file: ")
    file.write(text)

#3
file_name = input("Enter the file name: ")
lines = input("Enter the content as a list of lines using commas to seperated").split(',')
with open(file_name, 'w') as file:
    for line in lines:
        file.write(line + '\n')