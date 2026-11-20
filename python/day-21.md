# Day 21 · 装饰器与闭包

> 阶段：Python｜Python 基础到实战

## 学习目标

- 理解闭包与变量捕获
- 掌握装饰器语法 @
- 会写带参数的装饰器

## 今日知识点

- 函数嵌套与闭包
- @decorator 等价于 func = decorator(func)
- functools.wraps 保留元信息
- 带参装饰器三层嵌套

## 实践任务

1. 写 timer 装饰器统计函数执行时间
2. 写 log 装饰器打印函数调用日志
3. 用 wraps 保留被装饰函数名

## 验收标准

- timer 输出耗时
- log 输出调用信息
- __name__ 未被改变

## 推荐资源

- https://docs.python.org/3/glossary.html#term-decorator

## 今日打卡

- [ ] 完成今日知识点学习
- [ ] 完成全部实践任务
- [ ] 通过验收标准
- [ ] 学习时长：____ 小时
- [ ] 今日笔记 / 遇到的问题：
