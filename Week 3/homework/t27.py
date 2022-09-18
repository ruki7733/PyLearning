for x in range(49, 730):
    if x % 7 == x // 81 and (x // 7) % 7 == (x // 9) % 9 and x // 49 == x % 9:
        print(x)
        a = x // 49
        b = (x // 7) % 7
        c = x % 7
        # lst = [a, b, c]
        print(str(a) + str(b) + str(c))
        print(str(c) + str(b) + str(a))
