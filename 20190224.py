import random

print('现在让我们玩一个猜数字的游戏！')
random_num = random.randint(1, 100)
print('请输入1到100之间的任何数：')
i = 1
while True:
    num_guest = int(input())
    if num_guest < random_num:
        print('你输入的数字小了，再猜一次呢：')
    elif num_guest > random_num:
        print('你输入的数字大了，再猜一次呢：')
    else:
        print('恭喜你，猜对了！')
        print('正确答案就是 ' + str(random_num) + ',你用了' + str(i) + '就猜对了.')
        break
    i = i+1
