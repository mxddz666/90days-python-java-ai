# 待办事项：用 list 实现增删改查
todos = []


def show():
    if not todos:
        print("（暂无待办）")
        return
    for i, item in enumerate(todos, 1):
        print(f"{i}. {item}")


while True:
    print("\n1 添加  2 删除  3 查看  4 修改  5 退出")
    choice = input("请选择：").strip()

    if choice == "1":
        text = input("待办内容：").strip()
        if text:
            todos.append(text)
            print(f"已添加：{text}")
        else:
            print("内容为空，未添加")

    elif choice == "2":
        show()
        if todos:
            num = input("要删除第几项：").strip()
            if num.isdigit() and 1 <= int(num) <= len(todos):
                removed = todos.pop(int(num) - 1)
                print(f"已删除：{removed}")
            else:
                print("序号无效")

    elif choice == "3":
        show()

    elif choice == "4":
        show()
        if todos:
            num = input("要修改第几项：").strip()
            if num.isdigit() and 1 <= int(num) <= len(todos):
                new_text = input("新的内容：").strip()
                todos[int(num) - 1] = new_text
                print(f"已修改为：{new_text}")
            else:
                print("序号无效")

    elif choice == "5":
        print("退出")
        break

    else:
        print("无效选择")
