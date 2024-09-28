import sys
sys.setrecursionlimit(20000)
# 用于解决maximum recursion depth exceeded in comparison报错

# def openfile(addr = '../day2/user.txt',open_way = 'r+',encoding = "encoding='utf-8'"):
#     with (addr,open_way,encoding) as f:
#         data = f.readlines()
#         print(data)
#
# openfile()

def openfile(addr = '../day2/user.txt',open_way = 'r+',encoding = "encoding='utf-8'"):
    file = open(addr,open_way,encoding)
    for i in file.readlines():
        print(i)
openfile()