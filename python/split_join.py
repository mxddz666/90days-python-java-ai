# split 拆成列表，join 拼回字符串
s = "a,b,c"
parts = s.split(",")           # 按逗号切 → ['a', 'b', 'c']
result = "-".join(parts)       # 用短横线拼 → 'a-b-c'

print(f"原字符串：{s}")
print(f"split 后：{parts}")
print(f"join 后：{result}")

# 对照：split() 不传参数按空白切
words = "hello   world  python".split()
print(f"按空白切：{words}")
print(f"拼回空格：{' '.join(words)}")
