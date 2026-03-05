# my-react-app

Vite + React + TypeScript 项目。

## CI / GitHub Actions

项目使用 GitHub Actions 进行持续集成，工作流文件：`.github/workflows/ci.yml`。

### 触发条件

- 推送到 `main` / `master` 分支
- 针对 `main` / `master` 的 Pull Request

### 任务说明

| 任务 | 说明 |
|------|------|
| **build** | 安装依赖 → ESLint 检查 → TypeScript + Vite 构建 |
| **playwright** | 在 build 成功后运行 Python Playwright E2E 测试（Chromium） |

### 环境

- Node.js 20
- Python 3.12（Playwright 测试）
- Ubuntu latest
