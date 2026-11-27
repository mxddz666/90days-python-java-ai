# 用 set 去重：列表 → 集合 → 列表
nums = [3, 1, 2, 3, 2, 5, 1, 4, 3]
unique_nums = list(set(nums))

print(f"原列表：{nums}")
print(f"去重后：{unique_nums}")
print(f"元素个数：{len(nums)} → {len(unique_nums)}")

# set 无序，若想保留原顺序，用 dict.fromkeys（字典键不重复且保序）
ordered_unique = list(dict.fromkeys(nums))
print(f"保序去重：{ordered_unique}")

# 集合运算：交集 / 并集 / 差集
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"a = {a}, b = {b}")
print(f"交集 a & b：{a & b}")
print(f"并集 a | b：{a | b}")
print(f"差集 a - b：{a - b}")
