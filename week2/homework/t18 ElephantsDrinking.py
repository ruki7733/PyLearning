s=input().split()
h,r=float(s[0]),float(s[1])
Pi=3.14159
if (20*1000)%(Pi*r**2*h):
    num = (20 * 1000) / (Pi * r ** 2 * h)+1
    print("%d"%num)
else:
    num = (20 * 1000) / (Pi * r ** 2 * h)
    print("%d"%num)

