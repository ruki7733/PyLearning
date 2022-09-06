s=input()
if s[-1] in "Nn":
    g=float(s[0:-1])
    if g<=1000:
        print("8")
    elif g>1000:
        M1=int((g-1000)/500)*4+8
        if (g-1000)%500:
            M2=int(M1+4)
            print("%d"%M2)
        else:
            print("%d"%M1)
elif s[-1] in "Yy":
    g = float(s[0:-1])
    if g <= 1000:
        print("13")
    elif g > 1000:
        M1 = int((g - 1000) / 500) * 4+8+5
        if (g - 1000) % 500 :
            M2 = int(M1 + 4)
            print("%d"%M2)
        else:
            print("%d"%M1)