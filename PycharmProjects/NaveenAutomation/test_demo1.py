import pytest

@pytest.mark.login
def test_m1():
    a = 4
    b = 5
    assert a + 1 == b, "Test PASSED"
    assert a + 3 == b, "Test FAILED"


def test_m2():
    name = "Akash"
    assert name == "Akash", "Well done..!!!"


def test_login():
    assert "admin" == "admin"
