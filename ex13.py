from sys import argv # 和 input() 的区别是：在于用户输入的时机不同.
# read the WYSS section for how to run this
script, first, second, third = argv # 将它解包
# 脚本

# print(">>>>> argv=", repr(argv))
# >>>>> argv= ['.\\ex13.py', '1', '2', '3']
#                     ↑↑↑这是一个列表

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# argv、列表、解包、参数