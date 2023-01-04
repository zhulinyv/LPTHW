formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "threee", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

'''
在这个习题中用了一个叫函数（function）的东西，让它返回formatter变量到其它字符串中。当你看到formatter.format(...)的时候，这相当于我们告诉python做下面的事情。
1. 取第1行定义的formatter字符串。
2. 调用它的format函数，这相当于告诉它执行一个叫format的命令行命令。
3. 给format传递4个参数，这些参数和formatter变量中的{}相匹配，相当于将参数传递给了format这个命令。
4. 在formatter上调用format的结果是一个新字符串，其中的{}被4个变量替换掉了，这就是print现在打印的结果。
'''

# 格式化， formatter() 函数