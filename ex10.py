tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# 转义字符：                   功能：
# \\                          反斜杠(\)
# \'                          单引号(')
# \"                          双引号(BEL)
# \a                          ASCII 响铃符(BS)
# \b                          ASCII 退格符(FF)
# \f                          ASCII 进纸符(LF)
# \n                          ASCII 换行符
# \N{name}                    Unicode 数据库中的字符名，期中 name 是它的名字，仅 Unicode 适用
# \r                          ASCII 回车符(CR)
# \t                          ASCII 制表符(TAB)
# \uxxxx                      值为 16 位十六进制 xxxx 的字符
# \Uxxxxxxxx                  值为 32 位十六进制 xxxxxxxx 的字符
# \v                          ASCII 垂直制表符(VT)
# \ooo                        值为八进制值 ooo 的字符
# \xhh                        值为十六进制 hh 的字符

'''咱也布吉岛为什么，用三个引号注释就会报错，难道是转义字符的问题？'''

# 打印、转义