n=float(input())
if 0<=n<5:
    y=-n+2.5
    print("%.3f"%y)
elif 5<=n<10:
    y=2-1.5*(n-3)*(n-3)
    print("%.3f"%y)
elif 10<=n<20:
    y=n/2-1.5
    print("%.3f"%y)