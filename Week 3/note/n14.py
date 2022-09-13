s=input().split()
x,y,z=int(s[0]),int(s[1]),int(s[2])
n=m=max(x,y,z) #从三者立面最大的开始试
while True:
    if n%x==0 and n%y==0 and n%z==0:
        print(n)
        break
    n+=m #没必要一个个试，而是每隔m个试一下
