# test.py

def test_index_html_not_empty():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert len(content.strip()) > 0, "index.html está vacío"

def test_style_css_has_body_selector():
    with open('styles.css', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'body {' in content, "styles.css no contiene el selector 'body {'"
