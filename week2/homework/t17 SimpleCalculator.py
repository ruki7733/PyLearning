s=input().split()
a,b,c=int(s[0]),int(s[1]),s[2]
if c=="+":
    y=a+b
    print(int(y))
elif c=="-":
    y=a-b
    print(int(y))
elif c=="*":
    y=a*b
    print(int(y))
elif c=="/":
    if b==0:
        print("Divided by zero!")
    else:
        print(int(a//b))
else:
    print("Invalid operator!")