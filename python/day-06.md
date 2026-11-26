# Day 06 · 列表 list 与元组 tuple

> 阶段：Python｜Python 基础到实战｜日期：2026-11-26（周四）

## 学习目标

- 掌握列表的增删改查
- 理解列表可变、元组不可变
- 会用切片与常用方法

## 今日知识点

- list = [1, 2, 3]，append / insert / pop / remove
- 索引与切片 list[1:3]
- tuple = (1, 2, 3) 不可修改
- len() / in 运算符

## 实践任务

1. 写 todo.py：用列表实现待办事项的添加、删除、查看
2. 练习切片：取出列表的偶数索引元素
3. 尝试修改元组元素，观察报错信息

## 验收标准

- todo.py 能完成增删改查
- 切片结果正确
- 能复述元组不可变的报错内容

## 推荐资源

- https://docs.python.org/3/tutorial/introduction.html#lists

## 今日打卡

- [x] 完成今日知识点学习
- [x] 完成全部实践任务
- [x] 通过验收标准
- [x] 学习时长：____ 小时
- [x] 今日笔记 / 遇到的问题：list 可变，append 尾部加、insert 指定位置插、pop 按下标删并返回、remove 按值删；切片 [start:stop:step] 左闭右开，nums[::2] 取偶数索引（0,2,4…）、[1::2] 取奇数索引、[::-1] 倒序。tuple 不可变，改元素报 TypeError: 'tuple' object does not support item assignment，同样的下标赋值在 list 上就正常。todo.py 增删改查四功能都测过
