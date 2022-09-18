n = int(input())
if n == 1:
    print('End')
else:
    while True:
        s = n
        if s==1:
            print('End')
            break
        elif s % 2 == 0:
            n = n / 2
            print(str('%d'%s)+'/2='+str('%d'%n))
        elif s % 2 != 0:
            n = n * 3 + 1
            print(str('%d'%s)+'*3+1='+str('%d'%n))

