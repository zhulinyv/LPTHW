from sys import argv
from os.path import exists # exists() 将文件名字符串作为参数，如果文件名存在的话，它将返回True；否则将返回False。

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
print(">>>>> infile=", repr(in_file))
# indata = in_file.read()
# 简化代码，以上两行可以替换为下面一行。
indata = open(from_file).read() # 这样也无需运行下方的 in_file.close() 了，因为 read() 一旦运行，文件就会被Python关掉。

print(f"The input file is {len(indata)} bytes long") # len() 以 数值 的形式返回字符串的长度。

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
#                                               终止（还有流产的意思
input()

out_file = open(to_file, 'w').write(indata) # 简化代码，下面的 out_file.close() 也不用写了。
# out_file.write(indata)

print("Alright, all done.")

# out_file.close()
# in_file.close()
# 要养成关闭文件的习惯。