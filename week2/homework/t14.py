s=input().split()
a,b,c=int(s[0]),int(s[1]),int(s[2])
if a+b>c>a-b and a+b>c>b-a:
    print("yes")
else:
    print("no")
