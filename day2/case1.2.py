#将硬盘存放的该文件的内容一行一行地读入内存，修改完毕就写入新文件，最后用新文件覆盖源文件

import os

with open ('test') as read_f,open ('test.new', 'w') as write_f:
    for line in read_f:
        line = line.replace('Hello','NiHao')
        write_f.write(line)

os.remove('test')
os.rename('test.new','test.txt')

