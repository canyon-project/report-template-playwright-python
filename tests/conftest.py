import os
import subprocess
import time
import urllib.request

import pytest

os.environ["CANYON_OUTPUT_DIR"] = ".canyon_output"
pytest_plugins = ["canyonjs_playwright.pytest_plugin"]


@pytest.fixture(scope="session", autouse=True)
def dev_server():
    """在测试前自动启动 Vite 开发服务器"""
    proc = subprocess.Popen(
        ["npm", "run", "dev"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    url = "http://localhost:5173"
    for _ in range(60):
        try:
            urllib.request.urlopen(url, timeout=1)
            break
        except Exception:
            time.sleep(1)
    else:
        proc.kill()
        raise RuntimeError("开发服务器启动超时")
    yield
    proc.terminate()
