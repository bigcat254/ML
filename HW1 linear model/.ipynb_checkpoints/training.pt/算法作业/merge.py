import math
import random
import time
import numpy as np
import matplotlib.pyplot as plt

#插入排序代码
def Insert(arry):
    st = time.perf_counter()
    for i in range(len(arry)):
        j = i-1
        current = arry[i]
        while j >= 0 and arry[j] > current:
            arry[j+1] = arry[j]
            j = j - 1
        arry[j+1]= current
    ed = time.perf_counter()
    sort_time = ed - st
    return arry,sort_time

#合并排序代码

def MergeSort(array):
    if(len(array)<2):
        return array
    middle = math.floor(len(array)/2)
    left,righet = array[0:middle],array[middle:]
    arr = Merge(MergeSort(left),MergeSort(righet))
    return arr

def Merge(left,right):
    result =[]
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

def Partition(array,low,high):
    i = (low - 1)
    pivot = array[high]
    for j in range(low,high):
        if array[j] <= pivot:
            i += 1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[high] = array[high],array[i+1]
    return (i+1)
def QuickSort(array,low,high):
    st = time.perf_counter()
    if low >= high:
        pi = Partition(array,low,high)
        QuickSort(array,low,pi-1)
        QuickSort(array,pi+1,high)
    ed = time.perf_counter()
    sort_time = ed - st
    return array,sort_time

def Random_array(n):
    array = [random.randint(0,1000)for _ in range(n)]
    return array

if __name__ == '__main__':
    Insert_time = []
    merge_time = []
    Quick_time = []
    num  = []

    for i in range(1000,10000,500):
        num.append(i)
        array = Random_array(i)
        st = time.perf_counter()
        res1 = MergeSort(array)
        ed = time.perf_counter()
        time1 =ed - st
        merge_time.append(time1)
        res2,time2 = Insert(array)
        Insert_time.append(time2)
        res3,time3 = QuickSort(array,0,i-1)
        Quick_time.append(time3)



plt.rcParams['font.family'] = 'SimHei'
plt.plot(num, merge_time, label = "merge")
plt.plot(num, Insert_time, label = "insert")
plt.plot(num, Quick_time, label = "Quick")
plt.xlabel("num")
plt.ylabel("time")
plt.title("insert,quick,merge")
plt.legend()
plt.show()
