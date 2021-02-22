
# 去除字符串两端空格：

def trim1(string):
    if string[:1] == " ":
        return trim1(string[1:])
    elif string[-1:] == " ":
        return trim1(string[:-1])
    else:
        return string

def trim2(string):
    if string[:1] != " " and string[-1:] != " ":
        return string
    elif string[:1] == " ":
        return trim2(string[1:])
    else:
        return trim2(string[-1:])

# Fibonacci爬台阶：

# 递归
def fibo1(n):
    if n <= 3:
        return n
    else:
        return fibo1(n-2) + fibo1(n-1)

# 列表动态规划
def fibo2(n):
    if n <= 3:
        return n
    else:
        s = [1, 2]
        for i in range(3, n+1):
            s.append(s[-2] + s[-1])
        return s[-1]

# 动态规划
def fibo3(n):
    if n <= 3:
        return n
    else:
        n1 = 1
        n2 = 2
        i = 3
        while i <= n:
            tmp = n1
            n1 = n2
            n2 += tmp
            i += 1
        return n2

# 二分算法：

# 动态规划
def binarySearch(arr, x):
    l = 0
    r = len(arr)
    if r >= 1:
        mid = int((r - l) / 2)
        while(l > r):
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                r = mid - 1
            elif arr[mid] < x:
                l = mid + 1
    else:
        return -1

# 递归
def bnSrch(arr, l, r, x):
    if r >= 1:
        mid = int((r - l) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            bnSrch(arr, l, mid, x)
        elif arr[mid] < x:
            bnSrch(arr, mid, r, x)
    else:
        return -1

# 冒泡排序：

def bubbleSort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l

# 蓄水池：

def tank(l):
    vmax = 0
    for i in range(len(l)):
        for j in range(len(l)):
            h1 = l[i]
            h2 = l[j]
            if h1 >= h2:
                v = abs(i - j) * h1
            if v > vmax:
                vmax = v
    return vmax

# 判断是否两数平方和：

def Sq(n):
    sq = lambda x : not ((x ** 0.5) % 1)
    for i in range(int(n ** 0.5) + 1):
        if sq(n - i ** 2):
            return True
                
