import random

options = ['rock', 'paper', 'scissors']

print('Welcome to Finger')
print('本场游戏为三局两胜制')
print('请从以下选项中选择')
for i,option in enumerate(options):
    print(f"{i+1}.{option}")


player_i = 0
computer_i = 0
while player_i <3 and computer_i <3:
    # 玩家选择
    player = int(input('Enter your(1-3):')) - 1

    # 计算机随机选择
    computer = random.randint(0, 2)

    print(f'You chose {options[player]}')
    print(f'Computer chose {options[computer]}')

    #判断胜负
    if player == computer:
        print('Draw!')
        continue
    elif (player == 0 and computer == 1)or\
        (player == 1 and computer == 3)or\
        (player == 2 and computer == 0):
        print("You win!")
        player_i += 1
        continue
    else :
        print("You lose...")
        computer_i += 1
        continue
    break
print('你的胜场为%s'%player_i)
print('电脑胜场为%s'%computer_i)
if player_i > computer_i:
    print('你赢得了游戏的最终胜利！🎉')
if player_i < computer_i:
    print('很遗憾，你没有获得最终胜利…😢')