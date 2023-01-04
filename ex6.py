types_of_people = 10
x = f"There are {types_of_people} types of people."

bianry = "bianry"
do_not = "don't"
y = f"Those who know {bianry} and those who {do_not}."
#                     双性恋
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
# 令人捧腹的
joke_evaluation = "Isn't that joke so funny?!{}"
#     评价

# print(">>>>>",joke_evaluation,hilarious,''' sep="" ''') # sep='' 的作用是更改打印的每个变量之间的分隔样式.
print(joke_evaluation.format(hilarious))
# 详见：https://www.cnblogs.com/lovejh/p/9201219.html
w = "This is the left side of..."
e = "a string with a right side."

print(w+e)


'''
>>> print('{} {}'.format('hello','world'))  # 不带字段
hello world
>>> print('{0} {1}'.format('hello','world'))  # 带数字编号
hello world
>>> print('{0} {1} {0}'.format('hello','world'))  # 打乱顺序
hello world hello
>>> print('{1} {1} {0}'.format('hello','world'))
world world hello
>>> print('{a} {tom} {a}'.format(tom='hello',a='world'))  # 带关键字
world hello world
'''

# 打印、格式化字符串