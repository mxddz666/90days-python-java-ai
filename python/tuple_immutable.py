# 元组不可变：尝试修改元素会报错
point = (3, 5)

print(f"元组 point = {point}")

# list 可以改，tuple 不行
try:
    point[0] = 100
except TypeError as e:
    print(f"修改元组报错：TypeError: {e}")

# 对照：列表同一位置可以改
coords = [3, 5]
coords[0] = 100
print(f"列表可以改：{coords}")
