# 字典的键必须可哈希：能当键的 vs 不能当键的
ok = {
    "name": "Tom",     # 字符串，可哈希
    42: "answer",      # 整数，可哈希
    (1, 2): "tuple",   # 元组（里面都是不可变元素），可哈希
}
print(f"合法的键：{list(ok.keys())}")

# 列表不可哈希，不能当键
try:
    bad = {["a", "b"]: "value"}
except TypeError as e:
    print(f"列表当键报错：TypeError: {e}")

# 元组里含列表也不可哈希
try:
    bad = {(1, [2]): "value"}
except TypeError as e:
    print(f"含列表的元组当键报错：TypeError: {e}")
