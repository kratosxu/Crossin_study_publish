from random import choice
ur_score = 0
oppo_score = 0
shoot_order = [
    [0, 1, '你第一次射点球机会，加油！'],
    [0, 2, '你第二次射点球机会，加油！'],
    [0, 3, '你第三次射点球机会，加油！'],
    [0, 4, '你第四次射点球机会，加油！'],
    [0, 5, '你最后一次射点球机会，加油！'],
    [1, 1, '你对手第一次射点球，注意扑救！'],
    [1, 2, '你对手第二次射点球，注意扑救！'],
    [1, 3, '你对手第三次射点球，注意扑救！'],
    [1, 4, '你对手第四次射点球，注意扑救！'],
    [1, 5, '你对手第五次射点球，注意扑救！']
]
choices = ['左侧','中间','右侧']
print('点球大战准备开始！\n投掷硬币决定哪方先罚球，你准备好了吗？')
ur_shotting_choice = input('数字是正面，国徽是背面，你选正面还是背面？')
order = ('正面', '背面')
orderchoice = choice(order)
if orderchoice==ur_shotting_choice:
    shoot_order_rs = sorted(shoot_order, key=lambda x:(x[1], x[0]))
    print('结果是%s，你的先手' % orderchoice)
else:
    shoot_order_rs = sorted(shoot_order, key=lambda x: (x[1], x[0]*-1))
    print('结果是%s，你的对手的先手' % orderchoice)

for i in range (len(shoot_order_rs)):
    if shoot_order_rs[i][0]==0:
        print (shoot_order_rs[i][2])
        direc = input('你选择踢向球门的（左侧，中间，右侧）：')
        print ('好一个大力抽射！球冲着球门%s飞了过去' % direc)
        savedirec = choice(choices)

        if direc==savedirec:
            print('太可惜了！对方守门员也向球门%s扑了过去，你的点球被拦了下来' % direc)
        elif savedirec == '左侧' or savedirec == '右侧':
            print('球进了！好一个世界波！守门员做出了错误的判断，向球门%s做出扑救动作' % savedirec)
            ur_score += 1
        elif savedirec == '中间':
            print('牛×！球进了！守门员看到这脚世界波都蒙了，傻傻站在球门中间')
            ur_score += 1

        if ur_score > oppo_score:
            print('第%i局，比分：%i:%i，你暂时领先，赢到最后吧！' % (shoot_order_rs[i][1]+1, ur_score, oppo_score))
        elif ur_score > oppo_score:
            print('第%i局，比分：%i:%i，你暂时落后，加油！' % (shoot_order_rs[i][1]+1, ur_score, oppo_score))
        else:
            print('第%i局，比分：%i:%i，暂时平局，盘他！' % (shoot_order_rs[i][1]+1, ur_score, oppo_score))
    else:
        print(shoot_order_rs[i][2])
        direc = input('你选择球门的（左侧，中间，右侧）进行扑救：')
        savedirec = choice(choices)
        print('对方球员射出了点球，点球向着球门%s飞去' % savedirec)

        if direc==savedirec:
            print('你的守门员也向着球门%s扑救了过去。哼！太简单了！' % direc)
        elif direc == '左侧' or direc == '右侧':
            print('你的守门员向球门%s做出扑救动作。太可惜了，下次一定能扑救下来！' % savedirec)
        elif direc == '中间':
            print('你的守门员似乎笃定会从中路进攻，只可惜这次判断出现了偏差')

        if ur_score > oppo_score:
            print('第%i局，比分：%i:%i，你暂时领先，赢到最后吧！' % (shoot_order_rs[i][1]+1, ur_score, oppo_score))
        elif ur_score > oppo_score:
            print('第%i局，比分：%i:%i，你暂时落后，加油！' % (shoot_order_rs[i][1]+1, ur_score, oppo_score))
        else:
            print('第%i局，比分：%i:%i，暂时平局，盘他！' % (shoot_order_rs[i][1]+1, ur_score, oppo_score))