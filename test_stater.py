import pytest
from stater import delete_server


def test_delete_server():
    with pytest.raises(TypeError):
        delete_server("hello")
