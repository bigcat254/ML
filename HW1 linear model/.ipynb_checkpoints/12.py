import random
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

sys.setrecursionlimit(170000)


def InsertionSortRec(n, A):  # 递归算法
    if n > 1:
        InsertionSortRec(n - 1, A)
        x = A[n - 1]
        j = n - 2
        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = x


def InsertionSort(n, A):  # 非递归算法
    for i in range(1, n):
        temp = A[i]
        j = i - 1
        while j >= 0 and A[j] > temp:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = temp


# 设置组名
Time_1 = []
Num = []
Time_2 = []

for i in range(1, 5000, 100):
    Array = random.sample(range(0, 5000), i)  # 产生随机数，最大为500个
    Array_1 = Array[:]
    Array_2 = Array[:]
    Num.append(i)
    # 递归算法，并计算时间
    starTime_1 = time.time()
    InsertionSortRec(i, Array_1)
    endTime_1 = time.time()
    Time_1.append(endTime_1 - starTime_1)
    # 非递归算法，并计算时间
    starTime_2 = time.time()
    InsertionSort(i, Array_2)
    endTime_2 = time.time()
    Time_2.append(endTime_2 - starTime_2)
    print(i)

# 单位转化为
for i in range(len(Num)):
    Time_1[i] = Time_1[i] * 1000
    Time_2[i] = Time_2[i] * 1000

# 绘制图表

result_list_array =  np.array( Time_1)
result_list_array1 = np.array( Time_2)
plt.title('The relationship between time t(ms) and size N')
plt.xlabel('num (N)')
plt.ylabel('time(ms)')
plt.plot(Num, result_list_array, color='red',label='recursive')
plt.plot(Num, result_list_array1, color='blue',label='The iteration')
#plt.plot(Num, Time_1, label='Recursion')
#plt.plot(Num, Time_2, label='No_recursion')

plt.legend()
plt.show()




#ax.plot(result_list_array[:, 0], result_list_array[:, 1], color='red',label='recursive')
#ax.plot(result_list_array1[:, 0], result_list_array1[:, 1], color='blue',label='The iteration')
#plt.legend()
#plt.title('Fibonacci Time complexity comparison')
#plt.xlabel('number')
#plt.ylabel('time')
#plt.show()



