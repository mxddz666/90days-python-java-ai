# Day 23 · HTTP 请求与 requests 库

> 阶段：Python｜Python 基础到实战｜日期：2026-12-13（周日）

## 学习目标

- 理解 HTTP GET/POST 与状态码
- 掌握 requests 发送请求
- 会处理响应与异常

## 今日知识点

- requests.get(url, params=, headers=)
- response.status_code / json() / text
- POST 提交 data/json
- timeout 与异常处理

## 实践任务

1. GET 请求 GitHub API 获取一个公开仓库信息并打印 star 数
2. 带 params 发起带查询参数的请求
3. 捕获超时异常并打印友好信息

## 验收标准

- 能拿到真实 API 返回数据
- 状态码判断正确
- 超时被妥善处理

## 推荐资源

- https://requests.readthedocs.io/en/latest/user/quickstart/

## 今日打卡

- [ ] 完成今日知识点学习
- [ ] 完成全部实践任务
- [ ] 通过验收标准
- [ ] 学习时长：____ 小时
- [ ] 今日笔记 / 遇到的问题：
