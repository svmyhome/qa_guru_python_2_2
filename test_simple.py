import pytest

@pytest.fixture()
def open_browser():
    print("Фикстура до вызова")

@pytest.fixture()
def close_browser():
    yield
    print("после теста")

def test_first(open_browser):
    assert 1 == 1


def test_third(open_browser, close_browser):
    assert 1 == 1
