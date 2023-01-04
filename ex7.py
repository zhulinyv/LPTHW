print("Mary had a little lamb.") 
#                        羔羊
print("Its fleece was white as {}.".format('snow'))
#           羊毛
# print(">>>>>", f"Its fleece was white as {'snow'}.")
# print(">>>>>", "Its fleece was white as .".format('snow'))  # 可以运行......
# print(">>>>>", "Its fleece was white as {}.".format())  # 但如果用了.format()但不传入参数，会发生 index out of range （索引超出范围）.
print("And everywhere thay Mary went.")
print('.' * 10)  #what'd that do?  字符串乘以数字 == 重复的字符串.

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that commen at the end.  try removing it to see what happens  字符串可以相加
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')  # end='xxx'  不换行且替换为 '' 里的内容， '' 可换为 "" 
print(end7 + end8 + end9 + end10 + end11 + end12)

# Cheese Burger 奶酪汉堡

'''
q = "T"
w = "E"
e = "S"
r = "T"

print(q + w, end="*")
print(e + r)

>>>>> TE*ST
'''