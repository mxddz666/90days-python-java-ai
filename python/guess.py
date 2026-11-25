# 猜数字游戏：系统出 1-100 的数，最多猜 5 次
import random

answer = random.randint(1, 100)
max_tries = 5

for attempt in range(1, max_tries + 1):
    guess = int(input(f"第 {attempt} 次，猜一个数（1-100）："))

    if guess == answer:
        print(f"猜中了！答案就是 {answer}，用了 {attempt} 次")
        break
    elif guess < answer:
        print("猜小了，再大一点")
    else:
        print("猜大了，再小一点")
else:
    print(f"5 次用完，没猜中。答案是 {answer}")
