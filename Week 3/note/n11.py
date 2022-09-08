s=input().split()
n,m=int(s[0]),int(s[1])
for x in range(1,n):
    for y in range(x+1,n+1):
        if x<y and m%(x+y)==0:
            print(x,y)
            break