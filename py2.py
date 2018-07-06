import  random
computer = random.randint(0,2)
x = int(input("输入0-2"))
# 0 石头 1 剪刀 2 布
print("电脑出：%d" %computer)
if computer == x:
    print("平局")
elif computer == 0:
    if x == 1:
        print("输")
    elif x == 2:
        print("赢")
elif computer == 1:
    if x == 0:
        print("赢")
    elif x == 2:
        print("输")
elif computer == 2:
    if x == 1:
        print("赢")
    elif x == 0:
        print("输")
