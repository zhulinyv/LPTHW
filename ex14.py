from sys import argv

script, user_name = argv
# prompt = '> '
# 提示
prompt = f'{script}>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few qwestion.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f">>>>> How old are you? {user_name}")
age = int(input(prompt)) # 建议在这里转换为整数。。。咱也布吉岛为什么捏，这里转和下面转结果给了错误的变量报错是同样的捏~(￣▽￣)~*
# print(f"You're {int(age)}")
print(f"You're {age}")

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.    Not sure where that is.
And you have a {computer} computer.    Nice.
""")