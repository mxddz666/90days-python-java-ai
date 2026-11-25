# 猜数字游戏（自写版）：系统出 1-100 的数，最多猜 5 次
import random

answer = random.randint(1, 100)
max_tries = 5

for i in range(1, max_tries + 1):
    my = int(input("请输入一个数："))
    if my < answer:
        print("猜小了")
        continue
    elif my > answer:
        print("猜大了")
        continue
    else:
        print(f"猜对了是{answer}")
        break
else:
    print(f"五次结束，答案是{answer}")
