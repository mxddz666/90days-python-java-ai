# Day 13 · 封装、property 与特殊方法

> 阶段：Python｜Python 基础到实战

## 学习目标

- 理解私有属性约定 _ 与 __
- 掌握 @property 装饰器
- 会重写 __str__ / __len__ 等特殊方法

## 今日知识点

- _name 约定私有、__name 名称改写
- @property + @x.setter
- __str__ / __repr__ / __len__ / __eq__
- 运算符重载示意

## 实践任务

1. 给 Student 类用 @property 保护 score 属性（0-100 校验）
2. 重写 __str__ 让 print(student) 输出友好信息
3. 重写 __eq__ 让两个同分学生相等

## 验收标准

- score 赋值 150 会触发校验
- print 输出自定义格式
- 相等比较结果正确

## 推荐资源

- https://docs.python.org/3/tutorial/classes.html#private-variables-and-class-local-references

## 今日打卡

- [ ] 完成今日知识点学习
- [ ] 完成全部实践任务
- [ ] 通过验收标准
- [ ] 学习时长：____ 小时
- [ ] 今日笔记 / 遇到的问题：
