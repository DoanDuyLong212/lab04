#1
with open("python", "r") as file:
    file.seek(0)
    print(file.read())
#2
with open("python", "r") as file:
    file.seek(0, 2)
    print(file.read(10))
#3
with open("python", "r") as file:
    file.seek(-10, 1)
    print(file.read())
#4
with open('myfile.txt', 'r') as f:
    f.seek(-10, 2)
    last_10_chars = f.read()
#5
with open('myfile.txt', 'r') as f:
    f.seek(10)
    current_position = f.tell()
    print(f'Current position: {current_position}')