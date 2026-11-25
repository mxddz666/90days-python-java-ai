# Day 05 · 循环 for 与 while

> 阶段：Python｜Python 基础到实战｜日期：2026-11-25（周三）

## 学习目标

- 掌握 for 遍历与 while 条件循环
- 会用 range()
- 掌握 break / continue

## 今日知识点

- for i in range(10)
- while 条件: 循环体
- range(start, stop, step)
- break 跳出、continue 跳过本次

## 实践任务

1. 写 sum.py：用 for 计算 1 到 100 的和
2. 用 while 重写同一个求和程序
3. 写 guess.py：猜数字游戏，猜中 break，最多 5 次

## 验收标准

- 两个求和程序都输出 5050
- 猜数字游戏能正常结束
- 能说出 for 与 while 的适用场景

## 推荐资源

- https://docs.python.org/3/tutorial/controlflow.html#for-statements

## 今日打卡

- [x] 完成今日知识点学习
- [x] 完成全部实践任务
- [x] 通过验收标准
- [x] 学习时长：____ 小时
- [x] 今日笔记 / 遇到的问题：for 适合已知次数或遍历序列（range(1,101) 左闭右开），while 适合次数未知、靠条件终止（i<=100 手动 i+=1，忘了自增会死循环）。break 跳出整个循环，continue 跳过本次；for/while 后面的 else 只在循环"没被 break 打断"时执行，猜数字 5 次用完走 else。两个求和都得 5050；猜中/猜大猜小/5次用完三条路径都测过
