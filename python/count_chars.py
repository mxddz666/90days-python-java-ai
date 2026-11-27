# 统计一段文字中不重复的字符数
text = "python code is fun, python is powerful"

# 转成集合，重复的字符自动合并，len 就是不重复字符数
chars = set(text)
print(f"原文：{text}")
print(f"不重复的字符数：{len(chars)}")
print(f"这些字符是：{sorted(chars)}")

# 忽略大小写再统计：先统一转小写
chars_lower = set(text.lower())
print(f"忽略大小写后不重复的字符数：{len(chars_lower)}")

# 只统计字母：过滤非字母字符
letters = {c for c in text.lower() if c.isalpha()}
print(f"只算字母，不重复的字母数：{len(letters)}")
print(f"这些字母：{sorted(letters)}")
