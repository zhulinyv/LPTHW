from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0) # The function of .seek(0) is going to the 0th byte position of the file.

def print_a_line(line_count, f):
    print(line_count, f.readline()) # readline() 是从上一次开始的地方继续读取的, 而且会读取换行符。
                                    # 可用 .strip() 来移除。
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)