import pytest
from user_service import register_user

def test_register_user_success():
    register_user("userbaru", "password123")
    assert True

def test_register_user_empty_username():
    with pytest.raises(ValueError):
        register_user("", "password123")
