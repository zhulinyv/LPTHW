# Here's some new strange stuff, remeber type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" 
# \n开始字符串，可实现换行打印.

'''
test1 = "t1\nt2\"\nt3"
#要在字符串的引号中使用引号，需要在引号前使用 \ 转义.
print(">>>>>", test1)
'''
# 其它：
# test2 = "t1\nt2\\nt3"
# test3 = "t1\nt2\\\nt3"
# print(">>>>>", test2)
# print(">>>>>", test3)

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if you want, or 5,or 6.
""")
# ↑↑↑ 利用这个可以实现分行打印，可以实现字符串中有 " 或 ' ……，什么都可以有.

'''
print("""
      There's something going on here.
      With the three double-quotes(双引号).
      We'll be able to type as much as we like.
      Even 4 lines if you want, or 5,or 6.
      """)
'''
# Python不识别这些缩进，所以它们被当作字符串处理.
# 因此你的任何格式化都需要把文本对齐到左.

# 打印、转义