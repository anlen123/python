import os
file_name = input("输入你要转换的c语言的文件名:")
file_name2 = input("编译成的so文件的名字:")
shell = f"gcc -shared -Wl,-soname,{file_name2} -o {file_name2}.so -fPIC {file_name}"
print(shell)
os.system(shell)
