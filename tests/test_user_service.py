from user_service import register_user

def test_register():
    register_user("test", "123")
    assert True

