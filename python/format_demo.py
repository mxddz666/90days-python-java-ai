# 字符串常用方法与格式化

# 清洗：去首尾空格 + 首字母大写
raw = "   hello python world   "
cleaned = raw.strip().title()
print(f"原文：{repr(raw)}")
print(f"清洗后：{repr(cleaned)}")

# 各种大小写方法对比
s = "hello python"
print(f"upper(): {s.upper()}")
print(f"lower(): {s.lower()}")
print(f"title(): {s.title()}")
print(f"capitalize(): {s.capitalize()}")

# 查找与判断
text = "Python is powerful"
print(f"find('is'): {text.find('is')}")          # 找到返回下标
print(f"find('java'): {text.find('java')}")     # 找不到返回 -1
print(f"startswith('Python'): {text.startswith('Python')}")
print(f"endswith('powerful'): {text.endswith('powerful')}")

# 替换
print(f"replace: {text.replace('Python', 'Java')}")

# f-string 与 format 与 % 三种格式化
name, age = "Tom", 18
print(f"f-string: {name} is {age}")
print("format: {} is {}".format(name, age))
print("%% 格式化: %s is %d" % (name, age))
