# Day 04 · 条件分支 if / elif / else

> 阶段：Python｜Python 基础到实战｜日期：2026-11-24（周二）

## 学习目标

- 掌握单分支与多分支结构
- 理解布尔条件与缩进规则
- 能写嵌套判断

## 今日知识点

- if 条件: 语句块
- elif / else 的匹配顺序
- 缩进决定代码块（4 空格）
- 三元表达式 x if cond else y

## 实践任务

1. 扩展 bmi.py：BMI < 18.5 偏瘦，18.5-24 正常，>=24 偏胖
2. 写 score.py：输入分数输出 优秀/良好/及格/不及格
3. 用三元表达式重写一个简单 if-else

## 验收标准

- BMI 分级边界值测试正确（18.5、24）
- 分数程序覆盖四个等级
- 能说出缩进错误会导致什么

## 推荐资源

- https://docs.python.org/3/tutorial/controlflow.html#if-statements

## 今日打卡

- [x] 完成今日知识点学习
- [x] 完成全部实践任务
- [x] 通过验收标准
- [x] 学习时长：____ 小时
- [x] 今日笔记 / 遇到的问题：elif 从上往下匹配，命中即跳过；边界测试 BMI=18.5→正常、24→偏胖；score 90/75/60 边界正确；三元表达式 `"偶数" if n%2==0 else "奇数"`。缩进错误会抛 IndentationError（unexpected indent / unindent does not match any outer indentation level），Tab 与空格混用抛 TabError，代码块不成立
