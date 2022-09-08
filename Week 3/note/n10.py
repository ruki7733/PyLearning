total=0
s=input().split()
n,m=int(s[0]),int(s[1])
for n1 in range(1,n):
    for n2 in range(n1+1,n+1):
        if m%(n1+n2)==0:
            print(n1,n2)
            total+=1
            print(total)