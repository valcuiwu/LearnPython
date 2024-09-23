#将硬盘存放的该文件的内容全部加载到内存，在内存中是可以修改的，修改完毕后，再由内存覆盖到硬盘（word，vim，nodpad++等编辑器）

import os

with open('test') as read_f,open('test.new','w') as write_f:
    data = read_f.read()
    data = data.replace('NiHao','Hello')

    write_f.write(data)

os.remove('test')
os.rename('test.new','test')


