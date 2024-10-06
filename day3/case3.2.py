db = {}
# file = []
def operate_file(addr = '../day2/user.txt', mode = 'r+', encoding_argu = 'utf-8'):
    global file
    file = open(addr, mode, encoding=encoding_argu)
    #mode,encoding是open()方法的内置参数

    # for i in file.readlines():
    #     print(i)

    # print(file)

    data = file.readlines()
    # print(data)

    for i in data:
        ret = i.strip().split('|')
        # print(ret)
        db[ret[0]] = ret[1]
        print(db)

flag = 2
def match(name):
    global flag
    if name in db:
        flag = 1
    else:
        flag = 0
    return flag
#为什么这里return要缩进？

def login(name):
    i = 3
    while i:
        password = input('请输入密码：')
        if password == db[name]:
            print('登录成功')
            return
            #为什么此处ruturn没有直接结束login函数的调用，仍然在循环？
        else:
            print('密码错误！请重新输入')
            i -= 1
            print('已输错%s次，还剩%s次机会' % (3-i, i))
    if i<3:
        print('机会用尽，账户冻结！')


def register(name, password):
    # print('该用户不存在，请先注册！')
    # name = input('请输入要注册的用户名：')
    # password = input('请输入密码：')
    password_verify = input('请再次输入密码以确认：')
    if password == password_verify:
        print('注册成功！请重新登录吧')
        global flag
        flag = 1
        name_new = name
        password_new = password
        file.write(name_new + "|" + password_new + "\n")
        operate_file()
        login(name=name_new)
    return name, password



operate_file()

global name
name=input('请输入登录姓名:')
f = match(name)

while True:
    if f == 2:
        f = match(name=input('请输入用户姓名：'))

    elif f == 0:
        print('该用户不存在，请先注册！')
        # register(name=input('请输入要注册的新用户名：'), password=input('请输入密码：'))
        name_new, password_new = register(name=input('请输入要注册的新用户名：'), password=input('请输入密码：'))
        # operate_file()
        # login(name=name_new)
        break
    else:
        login(name)

file.close()


# 遇到的问题：
# 1. user.txt中，若光标位置另起一行，db[ret[0]] = ret[1]行位置报错：list index out of range
# 2. user.txt中，若光标位置紧接张三|123456，则有时会出现张三|123456李四|111111