# Day 52 · JVM 内存模型与 GC

> 阶段：Java｜Java 基础到 Spring Boot

## 学习目标

- 理解 JVM 内存区域
- 理解 GC 算法与分代收集
- 掌握基本 JVM 参数

## 今日知识点

- 堆/栈/方法区/程序计数器/本地方法栈
- 标记-清除/复制/标记-整理
- 新生代/老年代，Minor/Major GC
- -Xms / -Xmx / -XX:+PrintGCDetails

## 实践任务

1. 用 jvisualvm 或 jcmd 查看内存
2. 写一个产生大量临时对象的程序观察 GC
3. 设置堆大小并运行

## 验收标准

- 能说出堆与栈的区别
- 观察到 GC 日志
- JVM 参数生效

## 推荐资源

- https://docs.oracle.com/javase/specs/jvms/se17/html/

## 今日打卡

- [ ] 完成今日知识点学习
- [ ] 完成全部实践任务
- [ ] 通过验收标准
- [ ] 学习时长：____ 小时
- [ ] 今日笔记 / 遇到的问题：
