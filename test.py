# test.py

def test_index_html_not_empty():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert len(content.strip()) > 0, "index.html está vacío"

def test_index_html_has_bootstrap_css():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css' in content, "index.html no incluye el CSS de Bootstrap"

def test_index_html_has_bootstrap_js():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'https://code.jquery.com/jquery-3.5.1.slim.min.js' in content, "index.html no incluye el script de jQuery de Bootstrap"
        assert 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js' in content, "index.html no incluye el script de Bootstrap"

def test_index_html_has_navbar():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        assert 'class="navbar navbar-expand-lg navbar-light bg-light"' in content, "index.html no contiene la clase de la barra de navegación de Bootstrap"
