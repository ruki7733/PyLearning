tmpStr = input()
if tmpStr[-1] in ["F", "f"]:
    C = ((float(tmpStr[0:-1])) - 32) / 1.8
    print("转换后的温度是：" + str(C) + "C")
elif tmpStr[-1] in "Cc":
    F = ((float(tmpStr[0:-1])) * 1.8 + 32)
    print("转换后的温度是：" + str(F) + "F")
else:
    print("输入格式错误。")
