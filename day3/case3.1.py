import sys
sys.setrecursionlimit(20000)
# 用于解决maximum recursion depth exceeded in comparison报错

# def openfile(addr = '../day2/user.txt',open_way = 'r+',encoding = "encoding='utf-8'"):
#     with (addr,open_way,encoding) as f:
#         data = f.readlines()
#         print(data)
#
# openfile()

db={}
username = input('请输入用户名：')
password = 0
flag = 2

def openfile(addr = '../day2/user.txt',mode = 'r+',encoding_argu= 'utf-8'):
    file = open(addr,mode,encoding=encoding_argu)
    #mode,encoding是open()方法的内置参数

    # for i in file.readlines():
    #     print(i)

    data = file.readlines()
    # print(data)

    for i in data:
        ret = i.strip().split('|')
        # print(ret)
        db[ret[0]] = ret[1]
        print(db)

    def inf_match(name, flag):
        if name in db:
            nonlocal flag
            flag = 1
            def login(password):
                nonlocal password
                password = input('请输入密码：')
                if password == db[name]:
                    print('登录成功')
            return login
        else:
            nonlocal flag
            flag = 0
            def register(name,password):
                print('该用户不存在，请先注册！')
                name = input('请输入要注册的用户名：')
                password = input('请输入密码：')
                password_verify =input('请再次输入密码以确认：')
                if password == password_verify:
                    print('注册成功！请重新登录吧')
                    content = 'username|password'
                    file.write(content + '\n')
                    openfile()
                    login()
            return register

    print('flag =',flag)
    file.close()
    return inf_match



func = openfile()
#func = inf_match
func = func(username)

if flag == 1:
    func(password)
#(func = login) or (func = register)
if flag == 0:
    func(username,password)



