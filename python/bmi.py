# Day 02 练习：变量、数据类型与类型转换
# 输入身高(m)与体重(kg)，计算 BMI（体重 / 身高²），并输出保留 1 位小数的结果

height_input = input("请输入身高（米，如 1.75）：")
weight_input = input("请输入体重（千克，如 70）：")

# input() 返回值永远是 str，打印类型验证
print("height_input 的类型：", type(height_input))
print("weight_input 的类型：", type(weight_input))

# 显式转换为 float 才能参与数学运算
height = float(height_input)
weight = float(weight_input)

# BMI = 体重(kg) / 身高(m) 的平方
bmi = weight / (height ** 2)

# 转成保留 1 位小数的字符串输出
bmi_str = f"{bmi:.1f}"
print("你的 BMI 是：" + bmi_str)
print("BMI 字符串类型：", type(bmi_str))
