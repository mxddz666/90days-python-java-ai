#!/usr/bin/env bash
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
curl -sS --ssl-no-revoke \
  -X POST \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/user/repos \
  -d "{\"name\":\"$REPO_NAME\",\"description\":\"90 天 Python / Java / AI 学习计划\",\"private\":false}" >/dev/null || true

git add .
git commit -m "Init: 90 days Python Java AI learning plan" || true
git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin "https://${GITHUB_TOKEN}@github.com/${GITHUB_USER}/${REPO_NAME}.git"
git push -u origin main --force

echo "已推送：https://github.com/${GITHUB_USER}/${REPO_NAME}"
