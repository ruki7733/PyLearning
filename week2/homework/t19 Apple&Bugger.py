s=input().split()
n,x,y=int(s[0]),int(s[1]),int(s[2])
EatNum=y/x
LastApple=n-y/x
if LastApple>0:
    print("%d" % LastApple)
else:
    print("0")

