import time
import numpy as np
import matplotlib.pyplot as plt

#递归算法
def Fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fib(n - 1) + Fib(n - 2)

#递归时间记录
def function_Fib_Recursion(n):
    startTime = time.time()
    Fib(n)
    endTime = time.time()
    return endTime - startTime

#迭代算法时间记录
def function_Fib(n):
    startTime = time.time()
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
    endTime = time.time()
    return endTime - startTime

result_list_recursion = []
result_list = []

#记录0-30次的时间
for i in np.arange(0, 30, 3):
    user_time_recursion = function_Fib_Recursion(i)
    user_time = function_Fib(i)
    result_list_recursion.append([i, user_time_recursion])
    result_list.append([i, user_time])


# result_list_recursion
# result_list

#图像相关配置
result_list_array = np.array(result_list_recursion)
result_list_array1 = np.array(result_list)
fig, ax = plt.subplots()
plt.plot(result_list_array[:, 0], result_list_array[:, 1], color='red',label='recursive')
plt.plot(result_list_array1[:, 0], result_list_array1[:, 1], color='blue',label='The iteration')
#ax.plot(result_list_array[:, 0], result_list_array[:, 1], color='red',label='recursive')
#ax.plot(result_list_array1[:, 0], result_list_array1[:, 1], color='blue',label='The iteration')
plt.legend()
plt.title('Fibonacci Time complexity comparison')
plt.xlabel('number')
plt.ylabel('time')
plt.show()

# plt.plot(result_list_array[:, 0], result_list_array[:, 1])