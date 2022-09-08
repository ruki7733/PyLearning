m=int(input())
for i in range(m): #m组数据，要处理m次：第一次、第二次、第m次
    n=int(input()) #输入n
    total=0 #给total赋值为0
    for i in range(n): #n组数据，要处理n次
        total+=int(input())
    print(total)