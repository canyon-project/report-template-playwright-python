# report-template-playwright-python

Playwright Python + 覆盖率收集 Demo。

## 运行

```bash
# 1. 安装依赖
pnpm install
pip install -r requirements.txt
playwright install chromium --with-deps

# 2. 运行测试（会自动启动 Vite 开发服务器）
pytest tests/ -v
```

覆盖率数据输出到 `.canyon_output`。

关键配置：`tests/conftest.py` 中通过 `pytest_plugins = ["canyonjs_playwright.pytest_plugin"]` 注册 canyonjs_playwright 插件。
