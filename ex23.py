import sys
script, encoding, error = sys.argv

# sys.setrecursionlimit(100000) #设置递归深度

"""from sys import argv
script, encoding, error = argv"""


def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line: # 这里 if 的作用是检查这个字符串是否为空，以免无限执行下去。
             # 只要 readline() 返回了内容，则这里的结果就为 True .
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) # 在 main() 中调用 main() ，然后就变成了一个循环。
    # print(">>>>>> exit main")

def print_line(line, encoding, errors):
    next_lang = line.strip() # .strip() 用来移除每行收尾空格 和 \n
    # str1 = "00000003210Runoob01230000000"
    # print(str1.strip('0'))  # 去除首尾字符 0
    # >>>>>3210Runoob0123

    # str2 = "   Runoob      "   # 去除首尾空格
    # print(str2.strip())
    # >>>>>Runoob

    # .encode() 和 decode() 用法示例: http://c.biancheng.net/view/4305.html
    raw_bytes = next_lang.encode(encoding, errors = errors) # str.encode(encoding='UTF-8',errors='strict') # .encode() 编码
    """指定进行编码时采用的字符编码，该选项默认采用 utf-8 编码。例如，如果想使用简体中文，可以设置 gb2312。
       当方法中只使用这一个参数时，可以省略前边的“encoding=”，直接写编码格式，例如 str.encode("UTF-8")。

       指定错误处理方式，其可选择值可以是：
       strict：遇到非法字符就抛出异常。
       ignore：忽略非法字符。
       replace：用“？”替换非法字符。
       xmlcharrefreplace：使用 xml 的字符引用。
       该参数的默认值为 strict。"""
    cooked_string = raw_bytes.decode(encoding, errors = errors) # str.decode(encoding='UTF-8',errors='strict') # .decode() 解码
    """指定解码时采用的字符编码，默认采用 utf-8 格式。当方法中只使用这一个参数时，可以省略“encoding=”，直接写编码方式即可。
       注意，对 bytes 类型数据解码，要选择和当初编码时一样的格式。
       
       指定错误处理方式，其可选择值可以是：
       strict：遇到非法字符就抛出异常。
       ignore：忽略非法字符。
       replace：用“？”替换非法字符。
       xmlcharrefreplace：使用 xml 的字符引用。
       该参数的默认值为 strict。"""
    print(raw_bytes, "<===>", cooked_string)
        # 编码的字符串         # 解码的字符串

languages = open("languages.txt", encoding = "utf-8")
# print(">>>>>>", repr(languages))  # repr() 函数将对象转化为供解释器读取的形式。

main(languages, encoding, error)