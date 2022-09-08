import pytest

@pytest.fixture(scope="session", autouse=True)
def universal_browser():
    print("Стартует один раз за сессию")
    yield
    print("Завершает один раз за сессию")