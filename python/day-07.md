# Day 07 · 字典 dict 与集合 set

> 阶段：Python｜Python 基础到实战｜日期：2026-11-27（周五）

## 学习目标

- 掌握字典的键值对操作
- 掌握集合去重与集合运算
- 理解可变/不可变作为键的限制

## 今日知识点

- dict = {"name": "Tom"}，增删改查
- keys() / values() / items()
- set() 去重、& 交集 | 并集 - 差集
- 字典的键必须可哈希

## 实践任务

1. 写 contacts.py：用字典存储 3 个联系人，支持按姓名查询
2. 用 set 对含重复元素的列表去重
3. 统计一段文字中不重复的字符数

## 验收标准

- contacts.py 查询返回正确
- 去重结果无重复且顺序合理
- 能说出字典键为什么不能用列表

## 推荐资源

- https://docs.python.org/3/tutorial/datastructures.html#dictionaries

## 今日打卡

- [x] 完成今日知识点学习
- [x] 完成全部实践任务
- [x] 通过验收标准
- [x] 学习时长：____ 小时
- [x] 今日笔记 / 遇到的问题：dict 用键取值 contacts[name]，先 `in contacts` 判断键存在再取，否则 KeyError；keys()/values()/items() 分别拿键/值/键值对。set 自动去重但无序，去重 `[1,2,3,4,5]`；想保序用 dict.fromkeys 得 `[3,1,2,5,4]`。集合运算 & 交集、| 并集、- 差集都测过。set(text) 统计不重复字符，len 得 18，只算字母用 isalpha 过滤得 16。字典键必须可哈希：字符串/整数/元组可以，列表报 TypeError: unhashable type: 'list'，含列表的元组也不行；因为哈希值要固定才能定位键，列表可变。
