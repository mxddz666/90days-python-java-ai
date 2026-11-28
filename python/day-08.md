# Day 08 · 字符串处理与格式化

> 阶段：Python｜Python 基础到实战｜日期：2026-11-28（周六）

## 学习目标

- 掌握字符串常用方法
- 掌握 split / join / replace
- 熟练使用 f-string 与 format

## 今日知识点

- strip / lower / upper / title
- split() 按分隔符切分，join() 拼接
- find() / replace() / startswith()
- f-string 与 str.format()

## 实践任务

1. 写 wordcount.py：输入一句话，统计单词数并输出每个词
2. 把 "a,b,c" 用 split 转列表再用 join 拼回 "a-b-c"
3. 清洗字符串：去除首尾空格并把首字母大写

## 验收标准

- wordcount.py 单词数正确
- split/join 结果符合预期
- 字符串清洗结果正确

## 推荐资源

- https://docs.python.org/3/tutorial/introduction.html#strings

## 今日打卡

- [x] 完成今日知识点学习
- [x] 完成全部实践任务
- [x] 通过验收标准
- [x] 学习时长：____ 小时
- [x] 今日笔记 / 遇到的问题：split() 不传参按任意空白切，连续空格自动忽略，多个空格的句子仍数出 3 个词；传分隔符如 split(',') 按逗号切。join 是字符串方法，"-".join(['a','b','c']) → 'a-b-c'，顺序跟 split 反过来（split 字符串→列表，join 列表→字符串）。清洗用 strip() 去首尾空格 + title() 每个词首字母大写（capitalize() 只第一句首字母大写，两者不同）。find 找到返回下标、找不到 -1；startswith/endswith 返回布尔；replace 替换。三种格式化 f-string / format / % 都测过。踩坑：% 格式化里字面量 % 要写 %% 转义，否则报 ValueError: unsupported format character（写 "% 格式化" 时 % 后面跟了中文被当格式符）
