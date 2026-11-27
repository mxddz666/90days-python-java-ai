# 通讯录：用字典存 3 个联系人，支持按姓名查询
contacts = {
    "张三": "13800000001",
    "李四": "13800000002",
    "王五": "13800000003",
}

print("现有联系人：", "、".join(contacts.keys()))

while True:
    name = input("输入姓名查询（输入 q 退出）：").strip()
    if name == "q":
        print("退出")
        break

    # in 判断键是否存在，存在直接按 key 取值
    if name in contacts:
        print(f"{name} 的电话：{contacts[name]}")
    else:
        print(f"没找到 {name}")
