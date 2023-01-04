print("How old are you?", end=' ')
age = input()

# 利用 int() 可以将字符串转换为整数.
# age = int(input())
# print(">>>>> age=", repr(age))

print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# 输入 input()