age = input("How old are you? ")

# print(">>>>> How old are you? ", input())
'''
PS G:\Else\Files\lpthw> python .\ex12.py
10
>>>>> How old are you?  10
'''
# It doesn't work.

height = input("How tall are you? ")
# height = input(f"You're {age}? Nice! How tall are you? ")
# 似乎发现了格式化变量有什么用.

weight = input("How much do you weight? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# 输入