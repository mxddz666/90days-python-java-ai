# -*- coding: utf-8 -*-
"""生成 90 天 Python/Java/AI 学习计划仓库的全部 Markdown 文件。

用法：python scripts/generate_plan.py
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from plan_data import PYTHON, JAVA, AI  # noqa: E402

STAGES = [
    ("python", "Python 基础到实战", PYTHON, 1),
    ("java", "Java 基础到 Spring Boot", JAVA, 31),
    ("ai", "AI / 机器学习 / LLM", AI, 61),
]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def bullets(items):
    return "\n".join(f"- {item}" for item in items)


def numbered(items):
    return "\n".join(f"{i}. {item}" for i, item in enumerate(items, 1))


def day_file(stage_name, stage_title, start, index, data):
    day = start + index
    title, goals, learn, practice, check, resource = data
    stage_label = {"python": "Python", "java": "Java", "ai": "AI"}[stage_name]
    return f"""# Day {day:02d} · {title}

> 阶段：{stage_label}｜{stage_title}

## 学习目标

{bullets(goals)}

## 今日知识点

{bullets(learn)}

## 实践任务

{numbered(practice)}

## 验收标准

{bullets(check)}

## 推荐资源

- {resource}

## 今日打卡

- [ ] 完成今日知识点学习
- [ ] 完成全部实践任务
- [ ] 通过验收标准
- [ ] 学习时长：____ 小时
- [ ] 今日笔记 / 遇到的问题：

"""


def stage_readme(stage_name, stage_title, days, start):
    lines = [f"# {stage_title}", "", f"本阶段共 {len(days)} 天（Day {start:02d} - Day {start + len(days) - 1:02d}）。", "", "## 每日任务", ""]
    for i, data in enumerate(days):
        day = start + i
        lines.append(f"- [Day {day:02d} · {data[0]}](day-{day:02d}.md)")
    lines += ["", "## 阶段说明", "", "每天按「学习目标 → 知识点 → 实践任务 → 验收标准」顺序推进。", "完成后回到每日文件底部打卡，并在根目录 CHECKLIST.md 勾选对应日期。", ""]
    return "\n".join(lines)


def build_readme():
    return """# 90 天 Python / Java / AI 学习计划

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
"""


def build_roadmap():
    lines = ["# 90 天路线速查表", "", "| Day | 阶段 | 主题 |", "| --- | --- | --- |"]
    for stage_name, stage_title, days, start in STAGES:
        label = {"python": "Python", "java": "Java", "ai": "AI"}[stage_name]
        for i, data in enumerate(days):
            day = start + i
            lines.append(f"| {day:02d} | {label} | [{data[0]}]({stage_name}/day-{day:02d}.md) |")
    lines.append("")
    return "\n".join(lines)


def build_checklist():
    lines = ["# 90 天打卡清单", "", "完成一天勾选一项。", ""]
    for stage_name, stage_title, days, start in STAGES:
        lines += [f"## {stage_title}", ""]
        for i, data in enumerate(days):
            day = start + i
            lines.append(f"- [ ] Day {day:02d} · {data[0]}（[任务]({stage_name}/day-{day:02d}.md)）")
        lines.append("")
    return "\n".join(lines)


def build_setup():
    return """# 环境搭建指南

## 通用工具

| 工具 | 版本 | 用途 |
| --- | --- | --- |
| Git | 2.40+ | 版本管理 |
| VS Code | 最新版 | Python 编辑器 |
| IntelliJ IDEA Community | 最新版 | Java 编辑器 |
| Chrome / Edge | 最新版 | 查看文档与调试接口 |

## Python 环境

```bash
# Windows（PowerShell）
python -m venv .venv
.venv\\Scripts\\activate
pip install --upgrade pip
pip install requests beautifulsoup4 flask jupyterlab
```

Java 阶段和 AI 阶段依赖分开装，避免版本冲突：

```bash
# AI 阶段：单独环境
python -m venv .venv-ai
.venv-ai\\Scripts\\activate
pip install numpy pandas matplotlib seaborn scikit-learn torch transformers datasets fastapi uvicorn gradio joblib
```

验证安装：

```bash
python -c "import numpy, pandas, sklearn, torch, transformers; print('AI env OK')"
```

## Java 环境

1. 安装 JDK 17（LTS），验证 `java -version` 与 `javac -version`。
2. 安装 IntelliJ IDEA Community，新建 Maven 项目。
3. 安装 Maven 3.9+ 并加入 PATH，验证 `mvn -version`。
4. 在 `pom.xml` 中加入 JUnit 5 与 Spring Boot Starter 依赖（Day 53、Day 56 会用到）。

## 数据库

- SQLite：Python 内置 `sqlite3`，无需额外安装。
- MySQL / PostgreSQL：Java 阶段 JDBC 与 Spring Data JPA 任选其一，推荐先用 H2 内存数据库跑通流程。

## 浏览器与网络

- 安装 Postman 或直接用 `curl` 测试 REST API。
- 国内访问 Hugging Face 慢时配置镜像或代理，Day 82 会用到模型下载。

## 环境检查清单

- [ ] `python --version` 输出 3.11+
- [ ] `java -version` 输出 17
- [ ] `mvn -version` 可用
- [ ] Jupyter Lab 能启动
- [ ] `import torch` 无报错（AI 阶段）
"""


def build_cheatsheet():
    return """# 速查表

## Python 常用

```python
# 列表推导式
[x * 2 for x in range(10) if x % 2 == 0]

# 字典遍历
for k, v in d.items():
    print(k, v)

# 异常处理
try:
    ...
except ValueError as e:
    ...
finally:
    ...

# 上下文管理
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()
```

## Java 常用

```java
// 集合遍历
for (String s : list) { System.out.println(s); }

// Stream 过滤排序
list.stream().filter(x -> x > 80).sorted().collect(Collectors.toList());

// try-with-resources
try (BufferedReader br = Files.newBufferedReader(path)) {
    ...
}

// Lambda
Runnable r = () -> System.out.println("hello");
```

## PyTorch 训练循环

```python
for x, y in loader:
    optimizer.zero_grad()
    pred = model(x)
    loss = loss_fn(pred, y)
    loss.backward()
    optimizer.step()
```

## sklearn 标准流程

```python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = Pipeline([("scaler", StandardScaler()), ("model", LogisticRegression())])
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
```

## Git 常用

```bash
git status
git add .
git commit -m "Day 01 完成"
git push origin main
```
"""


def build_push_script():
    return """#!/usr/bin/env bash
# 把本仓库推送到 GitHub。
# 用法：GITHUB_USER=你的用户名 GITHUB_TOKEN=你的token bash scripts/push-to-github.sh
set -euo pipefail

GITHUB_USER="${GITHUB_USER:-}"
GITHUB_TOKEN="${GITHUB_TOKEN:-}"
REPO_NAME="90days-python-java-ai"
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"

if [ -z "$GITHUB_USER" ] || [ -z "$GITHUB_TOKEN" ]; then
  echo "缺少 GITHUB_USER 或 GITHUB_TOKEN 环境变量"
  echo "用法：GITHUB_USER=用户名 GITHUB_TOKEN=token bash scripts/push-to-github.sh"
  exit 1
fi

cd "$REPO_DIR"

# 本机证书吊销检查在代理环境下会失败，仓库级关闭
git config --local http.schannelCheckRevoke false

git init
git config --local user.name "$GITHUB_USER"
git config --local user.email "$GITHUB_USER@users.noreply.github.com"

# 通过 API 创建仓库（已存在则忽略错误）
curl -sS --ssl-no-revoke \\
  -X POST \\
  -H "Authorization: Bearer $GITHUB_TOKEN" \\
  -H "Accept: application/vnd.github+json" \\
  https://api.github.com/user/repos \\
  -d "{\\"name\\":\\"$REPO_NAME\\",\\"description\\":\\"90 天 Python / Java / AI 学习计划\\",\\"private\\":false}" >/dev/null || true

git add .
git commit -m "Init: 90 days Python Java AI learning plan" || true
git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin "https://${GITHUB_TOKEN}@github.com/${GITHUB_USER}/${REPO_NAME}.git"
git push -u origin main --force

echo "已推送：https://github.com/${GITHUB_USER}/${REPO_NAME}"
"""


def build_gitignore():
    return """.venv/
.venv-ai/
__pycache__/
*.pyc
.ipynb_checkpoints/
.env
*.log
.DS_Store
"""


def main():
    write(ROOT / "README.md", build_readme())
    write(ROOT / "ROADMAP.md", build_roadmap())
    write(ROOT / "CHECKLIST.md", build_checklist())
    write(ROOT / "SETUP.md", build_setup())
    write(ROOT / "resources" / "cheatsheet.md", build_cheatsheet())
    write(ROOT / "scripts" / "push-to-github.sh", build_push_script())
    write(ROOT / ".gitignore", build_gitignore())

    total = 0
    for stage_name, stage_title, days, start in STAGES:
        write(ROOT / stage_name / "README.md", stage_readme(stage_name, stage_title, days, start))
        for i, data in enumerate(days):
            day = start + i
            write(ROOT / stage_name / f"day-{day:02d}.md", day_file(stage_name, stage_title, start, i, data))
            total += 1

    print(f"生成完成：{total} 个每日任务文件，3 个阶段说明，6 个辅助文件")


if __name__ == "__main__":
    main()
