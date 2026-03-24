# report-template-playwright-python

在 [Playwright Python](https://playwright.dev/python/docs/intro)（pytest-playwright）中集成覆盖率收集，生成 `.canyon_output` 供后续报告生成或上报使用。

## 使用该方案的优势

对于端到端测试而言，该方案的核心优势包括：

- **支持现代化 Web 应用**：现代化的 Web 应用都会经过 JS bundle 打包，Playwright 提供的默认方案只能对原生 JS 等简单场景使用 V8 收集覆盖率，而该方案通过 Babel 插桩可以准确收集打包后代码的覆盖率
- **确保变更代码覆盖率完整性**：`@canyonjs/babel-plugin` 会在构建时生成一份初始覆盖率数据，确保在 CI 集成时，能够收集到因懒加载而可能丢失的变更代码覆盖率
- **与 pytest-playwright 无缝集成**：通过 pytest plugin 扩展 `page` fixture，在用户代码层面完全实现，不会修补或替换 pytest 测试运行器
- **灵活的覆盖率报告**：`.canyon_output` 中的覆盖率数据可配合 [Tools CLI](https://canyonjs.dev/docs/ecosystem/tools-cli) 聚合上报，或用于本地生成 HTML 报告

> **提示**：该方案特别适合使用现代构建工具（如 Vite、Webpack）的 React、Vue 等框架项目，能够准确追踪打包后代码的覆盖率情况。若你偏好 Python 编写 E2E 测试，可选用 [canyonjs-playwright-python](https://github.com/canyon-project/canyonjs-playwright-python)。

## 项目结构

```
├── src/                 # React 前端源码
├── tests/               # Playwright Python E2E 测试
│   ├── conftest.py      # pytest 配置与 canyonjs-playwright 插件
│   └── test_example.py  # 示例测试
├── vite.config.ts       # Vite 配置（含 Babel 插桩）
├── requirements.txt     # Python 依赖
└── .github/workflows/   # CI 配置
```

## 快速开始

### 环境要求

- Node.js 20+
- Python 3.12+
- pnpm 9+

### 安装依赖

```bash
# 前端依赖
pnpm install

# Python 依赖
pip install -r requirements.txt

# Playwright 浏览器（首次运行需要）
playwright install chromium --with-deps
```

### 运行测试

```bash
# 运行 Playwright E2E 测试（会自动启动 Vite 开发服务器）
pytest tests/ -v
```

测试运行后，覆盖率数据会输出到 `.canyon_output` 目录。

### 本地开发

```bash
# 启动 Vite 开发服务器
pnpm run dev

# 构建生产版本
pnpm run build
```

## 技术栈

| 类别 | 技术 |
|------|------|
| 前端框架 | React 19 + TypeScript |
| 构建工具 | Vite 7 |
| 测试框架 | pytest + pytest-playwright |
| 覆盖率收集 | @canyonjs/babel-plugin + babel-plugin-istanbul |
| 插件集成 | canyonjs-playwright |

## 配置说明

### Vite 插桩配置

在 `vite.config.ts` 中通过 `@vitejs/plugin-react` 的 Babel 选项启用插桩：

```ts
react({
  babel: {
    plugins: ['istanbul', '@canyonjs']
  }
})
```

### pytest 配置

在 `tests/conftest.py` 中：

1. 设置 `CANYON_OUTPUT_DIR` 指定覆盖率输出目录（默认 `.canyon_output`）
2. 注册 `canyonjs_playwright.pytest_plugin` 以扩展 `page` fixture
3. 使用 `dev_server` fixture 在测试前自动启动 Vite 开发服务器

## CI 集成

项目已配置 GitHub Actions，在 `main`/`master` 分支的 push 和 PR 时：

1. **build**：安装依赖、执行 lint、构建前端
2. **playwright**：安装 Python 依赖、运行 Playwright 测试

## 相关链接

- [Playwright Python 文档](https://playwright.dev/python/docs/intro)
- [canyonjs-playwright-python](https://github.com/canyon-project/canyonjs-playwright-python)
- [Canyon Tools CLI](https://canyonjs.dev/docs/ecosystem/tools-cli)
