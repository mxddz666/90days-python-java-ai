# 猜数字游戏：系统出 1-100 的数，最多猜 5 次
import random
aswer=random.randint(1,100)
max=5
for i in range(1,max+1):
    my=int(input("请输入一个数："))
    if my<aswer:
        print("猜小了")
        continue
    elif my>aswer:
        print("猜大了")
        continue
    else :
        print(f"猜对了是{aswer}")
        break
else :
    print(f"五次结束，答案是{aswer}")