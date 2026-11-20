# 环境搭建指南

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
.venv\Scripts\activate
pip install --upgrade pip
pip install requests beautifulsoup4 flask jupyterlab
```

Java 阶段和 AI 阶段依赖分开装，避免版本冲突：

```bash
# AI 阶段：单独环境
python -m venv .venv-ai
.venv-ai\Scripts\activate
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
