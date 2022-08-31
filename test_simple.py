import pytest

@pytest.fixture()
def open_browser():
    print("Фикстура 1 старт")
    yield
    print("Фикстура 1 конец")

@pytest.fixture()
def close_browser(open_browser):
    print("Фикстура 2 старт")
    yield
    print("Фикстура 2 конец")



def test_first(close_browser):
    assert 1 == 1


def test_third(open_browser, close_browser):
    assert 1 == 1
