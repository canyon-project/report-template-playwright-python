def test_homepage(page):
    page.goto("http://localhost:5173")
    assert "react" in page.title()
