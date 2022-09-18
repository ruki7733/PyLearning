n = input()
m = len(n)
lst = []
lst1 = ''
# print(m)
if n == 0:
    print(0)
elif n[0] == '-':
    for i in range(1, m):
        lst.insert(i, n[m - 1])
        lst1 = ''.join(lst)
        m -= 1
    print(0 - int(lst1))
else:
    for i in range(m):
        lst.insert(i, n[m - 1])
        lst1 = ''.join(lst)
        m -= 1
    print(int(lst1))
