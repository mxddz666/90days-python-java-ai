height = float(input("输入你的身高："))
weight = float(input("输入你的体重："))
bmi = weight / (height * height)

if bmi < 18.5:
    level = "偏瘦"
elif bmi < 24:
    level = "正常"
else:
    level = "偏胖"

print(f"您的 BMI 是 {bmi:.1f}，{level}")
