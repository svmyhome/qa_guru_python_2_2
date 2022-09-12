import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.timeout = 4  # к каждой команде применяется ожидание  4 секунды
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1900
    browser.config.window_height = 1000
    #browser.config.browser_name = 'firefox' # выбор браузера на котором запускать

    yield