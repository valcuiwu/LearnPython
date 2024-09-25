db={}

with open('user.txt', 'a+', encoding='utf-8') as f:
    data = f.readlines()
    print(data)
    for i in data:
        ret = i.strip().split('|')
        db[ret[0]] = ret[1]
        print(db)

    while True:
        username = input('请输入用户名：')

        if username in db:
            i = 3
            while i:
                password = input('请输入密码：')

                if password == db[username]:
                    print('登录成功')
                    break
                else:
                    print('密码错误！')
                    i -= 1
                    print('还剩%s次机会！'%i)
                    if i == 0:
                        print('机会用尽，账户冻结！')
            break
        else:
            print('用户名不存在,请先注册！')
            new_username = input('请输入新用户用户名:')
            new_password = input('请输入新用户密码:')
            f.write(new_username + "|" + new_password + "\n")