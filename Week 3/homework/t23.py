n = int(input())
s = input().split()
a, b = int(s[0]), int(s[1])
x = b / a
for i in range(1, n ):
    s1 = input().split()
    a1, b1 = int(s1[0]), int(s1[1])
    y = b1 / a1
    if y - x > 0.05:
        print('better')
    elif x - y > 0.05:
        print('worse')
    else:
        print('same')
