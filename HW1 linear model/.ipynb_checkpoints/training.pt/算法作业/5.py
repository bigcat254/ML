import time
import random
import sys
sys.setrecursionlimit(1000000)
from matplotlib.font_manager import FontProperties
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
#递归算法求最长公共子序列长度
def rec_LCS(i,j):
    lena = len(a)
    lenb = len(b)
    if i>=lena or j>=lenb:
        return 0
    if a[i]==b[j]:
        return 1+rec_LCS(i+1,j+1)
    elif rec_LCS(i+1,j)>rec_LCS(i,j+1):
        return rec_LCS(i+1,j)
    else:
        return rec_LCS(i,j+1)

#动态规划求最长公共子序列长度
def LCS(string1,string2):
    len1 = len(string1)
    len2 = len(string2)
    book = [[0 for i in range(len1+1)] for j in range(len2+1)]
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if string2[i-1] == string1[j-1]:
                book[i][j] = book[i-1][j-1]+1
            else:
                book[i][j] = max(book[i-1][j],book[i][j-1])
    return book[-1][-1]

def Memory(n,c,w,v,memo):
    if c <=0 or n < 0:
        return  0
    if memo[n][c] != -1:
        return memo[n][c]
    res = Memory(n-1,c,w,v,memo)
    if(w[n-1] <= c):
        res = max(res, v[n-1]+ Memory(n -1 ,c-w[n-1],w,v,memo))
    memo[n][c] = res
    return res
#函数运算时间
def time_Counter(func, x, y):
    time_start = time.time()
    func(x,y)
    time_end = time.time()
    return time_end-time_start

#生成一个指定长度的随机字符串
def generate_random_str(randomlength=16):
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str



if __name__=='__main__':
    N = []
    time1 = []
    time2 = []
    time3 = []
    for i in range(1,10,1):

        a = generate_random_str(i)
        b = generate_random_str(i)

        #time1.append(1)
        time1.append(time_Counter(rec_LCS,0,0))
        time2.append(time_Counter(LCS,a,b))


        N.append(i)

    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.title('Longest common subsequence algorithm comparison')
    plt.xlabel('num (N)')
    plt.ylabel('time(ms)')
    plt.plot(N, time1, label='rec_LCS')
    plt.plot(N, time2, label='Memory')
    plt.plot(N, time2, label='LCS')
    plt.legend()
    plt.show()
    #算法测试
    a = generate_random_str(10)
    b = generate_random_str(10)

    print('字符串a:',a)
    print('字符串b:',b)
    print('递归算法求得的最长公共子序列长度:',rec_LCS(0,0))
    print('动态规划算法求得的最长公共子序列长度:',LCS(a,b))

    print('递归实现最长公共子序列算法所耗时间：',time1)
    print('动态规划实现最长公共子序列算法所耗时间：',time2)
