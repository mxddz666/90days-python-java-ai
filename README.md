# 90 天 Python / Java / AI 学习计划

一条 90 天的工程化自学路线：Python 打底 → Java 建立工程思维 → AI 落地。每天有明确任务、实践内容和验收标准，学完即产出 3 个可展示项目。

## 路线总览

| 阶段 | 天数 | 方向 | 结业产出 |
| --- | --- | --- | --- |
| 第一阶段 | Day 01 - Day 30 | Python 基础到实战 | 命令行待办工具 |
| 第二阶段 | Day 31 - Day 60 | Java 基础到 Spring Boot | 图书管理系统 |
| 第三阶段 | Day 61 - Day 90 | AI / 机器学习 / LLM | 情感分析系统 + 智能问答机器人 |

## 每日结构

每个 `day-XX.md` 包含五部分：

1. 学习目标 - 今天要拿到什么结果
2. 今日知识点 - 需要掌握的概念
3. 实践任务 - 必须动手完成的事
4. 验收标准 - 判断是否过关的硬指标
5. 推荐资源 - 权威文档与教程链接

## 怎么使用

1. 先看 [SETUP.md](SETUP.md) 配好环境。
2. 从 [Day 01](python/day-01.md) 开始，一天一个文件。
3. 每天结束后在当日文件底部打卡，并在 [CHECKLIST.md](CHECKLIST.md) 勾选。
4. 每 30 天做一次阶段复盘，未达验收标准就重做卡壳的任务。
5. 完整 90 天路线见 [ROADMAP.md](ROADMAP.md)。

## 仓库结构

```
.
├── README.md          本文件
├── ROADMAP.md         90 天路线速查表
├── CHECKLIST.md       打卡清单
├── SETUP.md           环境搭建指南
├── python/            Day 01-30 + 阶段说明 + 项目
├── java/              Day 31-60 + 阶段说明 + 项目
├── ai/                Day 61-90 + 阶段说明 + 项目
├── resources/         速查表
└── scripts/           生成脚本 + 推送脚本
```

## 三个实战项目

| 项目 | 技术栈 | 位置 |
| --- | --- | --- |
| 命令行待办工具 | Python + JSON | Day 29 |
| 图书管理系统 | Java + Spring Boot + JPA | Day 59 |
| 情感分析系统 / 问答机器人 | PyTorch + Hugging Face + RAG + FastAPI | Day 88-89 |

## 更新计划

重新生成全部 Markdown：`python scripts/generate_plan.py`

推送到 GitHub：`GITHUB_USER=<用户名> GITHUB_TOKEN=<token> bash scripts/push-to-github.sh`
