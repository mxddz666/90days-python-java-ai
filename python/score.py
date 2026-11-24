# Day 04 练习：条件分支 if / elif / else
score = float(input("输入分数："))

if score >= 90:
    level = "优秀"
elif score >= 75:
    level = "良好"
elif score >= 60:
    level = "及格"
else:
    level = "不及格"

print(f"分数 {score}，等级：{level}")

# 三元表达式重写简单 if-else：判断奇偶
number = int(input("输入一个整数："))
parity = "偶数" if number % 2 == 0 else "奇数"
print(f"{number} 是{parity}")
