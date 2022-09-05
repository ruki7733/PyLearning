year=int(input())
if year<=0:
    print("输入年份有误")
else:
    if year>1949 and (year-1949)%10==0:
        num =int((year-1949)/10)
        print("建国"+str(num)+"周年")
    elif year > 1921 and (year-1921)%10==0:
        num=int((year-1921)/10)
        print("建党"+str(num)+"周年")
    elif year % 4==0 and year%100 or year%400==0:
        print("闰年")
    else:
        print("普通年份")
