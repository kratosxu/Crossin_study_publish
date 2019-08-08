op = open('c:/Users/suhao.xu/desktop/MIDTERM01.TXT','r')
# 逻辑为：
# 1. 打开文件读取每一行，表头行添加名次，总分，平均分和排序用的数字0，
# 2. 求每个人的平均分和总分，最后添加排序用的数字1
# 3. 求平均行各科的平均分和总分，最后添加排序用的数字2
# 4. 替换低于60分的成绩为不及格
# 5. 根据每一行的最后一列和倒数第二列进行排序
# 6. 把结果转换成一个长字符串，并且去掉之前用于排序的最后一列
# 7. 写入文件

# rs为二元序列的最终结果
rs = []
# table_index变量为表头的序列
table_index = ['名次']

# 完善表头序列，取出每个人的成绩，并且计算每个人的总分和平均分
for i in op.readlines():
    score_pp = list(i.split())
    if score_pp[0] == '姓名':
        table_index.extend(x for x in score_pp)
        table_index.extend(['总分', '平均分', 0])
    else:
        score_content = []
        score_content.append(score_pp[0])
        sum_score = 0
        for j in score_pp[1:]:
            sum_score += int(j)
            score_content.append(int(j))
        avg_score = round(sum_score/(len(score_pp)-1),1)
        score_content.extend([sum_score, avg_score, 2])
        rs.append(score_content)
op.close()
print(rs)

# 求“平均”行的数据
score_avg = ['平均']
for m in range(1, len(rs[0])-2):
    avg_subject = 0
    for n in range(1, len(rs)-1):
        avg_subject += float(rs[n][m])
    score_avg.append(round(avg_subject/(len(rs)),1))
score_avg.extend([round(sum(score_avg[1:-1])/(len(score_avg[1:-1])-1)),
                 1])

# 替换低于60分的成绩为“不及格”，并且把“平均”行添加到rs中
for i in range(1, len(rs)-1):
    for j in range(1, len(rs[i])-3):
        if rs[i][j]<60:
            rs[i][j] = '不及格'
rs.append(score_avg)

# 以rs中每个子序列的最后一个数字作为排序的第一条件，倒数第二个数字作为排序的第二条件进行排序
rs.sort(key=lambda x : (x[-1], -x[-2]))
rs.insert(0, table_index)
print (rs)

# wr_str为最后写入文件用的长字符串，rk为“名次”列的序号
wr = open('c:/Users/suhao.xu/desktop/MIDTERM01_RS.TXT','w')
wr_str=''
rk = 0
for x in range(len(rs)):
    if x == 0:
        for y in range(len(rs[x])-1):
            wr_str += str(rs[x][y]) + ' '
    else:
        wr_str += '\n' + str(rk) + ' '
        for z in range(len(rs[x])-1):
            wr_str += str(rs[x][z]) + ' '
        rk += 1
wr.writelines(wr_str)
wr.close()



