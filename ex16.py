from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want thay, hit CTRL- (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')
# 'w' 是 “写入”（write）模式，'r' 表示 “读取”（read），'a' 表示 “追加”（append）.
# 以 “写入” 模式创建文件时，不存在的文件将会被创建.

print("Truncating the file.    Goodbye!")
target.truncate() # 需要上面指定写入模式才可以用，否则报错：io.UnsupportedOperation: truncate.

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}\n") # 简化代码.
'''
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''

print("And finally, we close it.")
target.close()
# 即使注释掉上面一行，不进行文件关闭命令，文件内容依旧会被保存。BUT remember,you should save your file by yourself.
# 因为如果你不关闭你的文件，你的程序将会越来越复杂，文件也就会泄露，然后计算机就崩溃了。
# （如后面讲到While循环的时候）
# 养成好习惯！！

'''
close: 关闭文件。跟你的编辑器中的 “文件” → “保存” 是一个意思。
read: 读取文件的内容。你可以把结果赋给一个变量。
readline: 只读取文本文件中的一行。
truncate: 清空文件，请小心使用该命令。
write('stuff'): 将 “stuff” 写入文件。
seek(0): 将读写位置移动到文件开头。 
'''