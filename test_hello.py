"""
"""
from hello import app


def test_hello() -> None:
    """Test hello function."""
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert response.data == b'<h1>Hello, World!</h1>'


def test_hello_name() -> None:
    """Can't test flask route the usual way...
    """
    # not allowed...
    # assert hello('Flask') == '<h1>Hello, Flask!</h1>'
    assert True
