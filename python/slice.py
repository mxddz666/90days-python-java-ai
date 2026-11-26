# 切片练习：取出列表的偶数索引元素
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 偶数索引 = 下标 0,2,4...，用 [::2] 一步取出
even_index = nums[::2]

print(f"原列表：{nums}")
print(f"偶数索引元素：{even_index}")

# 对照：奇数索引用 [1::2]
odd_index = nums[1::2]
print(f"奇数索引元素：{odd_index}")

# 切片 [1:4] 是左闭右开，含 1 不含 4
print(f"nums[1:4]：{nums[1:4]}")
print(f"nums[-3:]：{nums[-3:]}")
print(f"nums[::-1] 倒序：{nums[::-1]}")
