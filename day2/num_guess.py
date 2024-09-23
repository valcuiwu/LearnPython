import random

while True:
    num = random.randint(1, 100)
    i = 5
    while i:
        # print(num)
        print('还剩%s次机会' % i)
        guess = int(input("请猜一个数字:（0-100） "))
        if guess < num:
            print('猜小了')
            i -= 1
            continue
        elif guess > num:
            print('猜大了')
            i -= 1
            continue
        else:
            print('猜对啦')
        break
    # print(i)
    if i==0:
        print('尝试次数已达上限，请重来一次吧')
        num = random.randint(1, 100)
        continue
    break
