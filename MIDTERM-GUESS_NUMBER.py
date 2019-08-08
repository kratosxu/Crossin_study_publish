import random as rd
import os

username = input('请输入您的名字：')
dictionary = {}
if os.path.exists('game.txt')==True:
    with open ('game.txt', 'r', encoding='gbk') as f:
        for i in f.readlines():
            a = str(i).split()
            dictionary[a[4]] = [a[0], a[1], a[2], a[3]]

        if username in dictionary:
            total_games = int(a[0])
            fastest = int(a[1])
            guess_times = int(a[2])
            win_times = int(a[3])
            print('欢迎回来%s，祝你游戏愉快！' % (username))
        else:
            total_games = 0
            fastest = 6
            guess_times = 0
            win_times = 0
            dictionary[username]= ['0', '0', '0', '0']
            print('欢迎你%s，准备好猜数字的游戏了吗？' % (username))
else:
    op = open('game.txt', 'w')
    total_games = 0
    fastest = 6
    guess_times = 0
    win_times = 0
    dictionary[username] = ['0', '0', '0', '0']
    print('欢迎你%s，准备好猜数字的游戏了吗？' % (username))
    op.close()

if total_games != 0:
    avg_times = guess_times / float(total_games)
else:
    avg_times = 0


def number_input():
    while True:
        num = input('请输入10以内的整数数字：')
        try:
            num = int(num)
            if num >= 1 and num <= 10:
                break
            else:
                print('不要调皮！看清提示哦！')
        except:
            print('不要调皮！看清提示哦！')
    return num

continue1 = 'Y'
while continue1=='Y':
    answer = rd.randint(1,10)
# 一共5次猜测机会，但是循环6次，第六次判断是为了判断是否还玩的逻辑
    for i in range(1,7):
        if i<6 and continue1!='N':
            print('第%d次游戏' % (i))
            ipt=number_input()
            if ipt>answer :
                print('太大了')
                # print(answer)
            elif ipt<answer :
                print('太小了')
                # print(answer)
            elif ipt == answer :
                print('猜中了！答案就是%d\n你猜中答案一共用了%d次机会'
                      % (answer, i))
                # print (answer)
                total_games += 1
                guess_times += i
                win_times +=1
                if fastest>i:
                    fastest = i
                print ('你一共玩了%d次游戏\n平均%.1f次猜对\n最好成绩是%d次'
                       % (total_games, guess_times/total_games, fastest))
                break
        else:
            if win_times == 0:
                total_games += 1
                print('抱歉，你本次没猜对\n答案是%d\n你一共玩了%d次'
                      % (answer, total_games))
            else:
                total_games += 1
                guess_times += 5
                print('抱歉，你本次没猜对\n答案是%d\n你一共玩了%d次游戏\n平均%.1f次猜对\n最好成绩是%d次'
                      % (answer, total_games, guess_times/total_games, fastest))

    continue1 = input('是否继续本轮游戏？（Y:是，N：否）')
    while continue1 != 'Y' and continue1 != 'N':
        continue1 = input('输入错误（请注意是大写哦~）\n是否继续本轮游戏？（Y:是，N：否）')


print ('GAME OVER, 您本轮游戏结束')
print ('你一共玩了%d次游戏\n平均%.1f次猜对\n最好成绩是%d次'
       % (total_games, guess_times/total_games, fastest))



with open ('game.txt', 'w', encoding = 'gbk') as f:
    writting = ''
    for i in dictionary.keys():
        if i == username:
            writting = writting + str(total_games) + ' ' + str(fastest) + ' '\
                       + str(guess_times) + ' ' + str(win_times) + ' ' + i + '\n'
        else:
            writting = writting + dictionary[i][0] + ' ' + dictionary[i][1] + ' ' \
                       + dictionary[i][2] + ' ' + dictionary[i][3] + ' ' + i + '\n'

    f.writelines(writting)