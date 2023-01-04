from sys import argv

script, filename = argv

# txt = open(filename)
txt = open(filename, encoding="UTF-8") # encoding= 可以指定编码格式，使 Python 成功读取中文、日文等文档.

print(f"Here's your file {filename}:")
# print(txt.read(6)) # 指定整数可以读取对应字节的内容
print(txt.read()) # 经过测试，先制定数字，再设为空，.read 会接着上一次的内容继续读取而不是从头开始.

txt = open(filename, encoding="UTF-8")
print(txt.read())

txt = open(filename, encoding="UTF-8")
txt.close()
# print(txt.read()) # 不可以对关闭的文本进行 I/O(输入或输出) 操作.

'''
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
'''
# Python 不会限制让你只打开一次文件