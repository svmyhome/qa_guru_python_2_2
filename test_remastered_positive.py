import pytest
from selene.support.shared import browser
from selene import be, have
import time

name_form = "Practice Form"
fill_in_form_title = "Thanks for submitting the form"
first_name = "Ivan"
last_name = "Ivanov"
user_email = "Ivanov@.mail.ru"
gender = "Male"
student_name = "Ivan Ivanov"
mobile = "1234567890"


@pytest.fixture()
def open_browser():
    browser.config.browser_name = 'chrome'

@pytest.fixture()
def configure_mobile_browser(open_browser):
    browser.config.window_width = 375
    browser.config.window_height = 667
    browser.open('https://demoqa.com/automation-practice-form')

@pytest.fixture()
def configure_desktop_browser(open_browser):
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://demoqa.com/automation-practice-form')


def test_first_page_mobile(configure_mobile_browser):
    assert name_form == browser.element("//div[text()='Practice Form']").text
    browser.element("//input[@id = 'firstName']").type(first_name)
    browser.element("//input[@id = 'lastName']").type(last_name)
    browser.element("//input[@id = 'userEmail']").type(user_email)
    browser.element("//label[text() = '" + gender + "']").click()
    browser.element("//input[@id = 'userNumber']").type(mobile).press_enter()
    time.sleep(1)  # разве селен не автоматический выставляет задержку
    assert fill_in_form_title == browser.element("//div[@id='example-modal-sizes-title-lg']").text
    assert student_name == browser.element("//td[text()='Student Name']/following-sibling::td").text
    assert user_email == browser.element("//td[text()='Student Email']/following-sibling::td").text
    assert gender == browser.element("//td[text()='Gender']/following-sibling::td").text
    assert mobile == browser.element("//td[text()='Mobile']/following-sibling::td").text
    time.sleep(3)

def test_first_page_desktop(configure_desktop_browser):
    assert name_form == browser.element("//div[text()='Practice Form']").text
    browser.element("//input[@id = 'firstName']").type(first_name)
    browser.element("//input[@id = 'lastName']").type(last_name)
    browser.element("//input[@id = 'userEmail']").type(user_email)
    browser.element("//label[text() = '" + gender + "']").click()
    browser.element("//input[@id = 'userNumber']").type(mobile).press_enter()
    time.sleep(1) # разве селен не автоматический выставляет задержку
    assert fill_in_form_title == browser.element("//div[@id='example-modal-sizes-title-lg']").text
    assert student_name == browser.element("//td[text()='Student Name']/following-sibling::td").text
    assert user_email == browser.element("//td[text()='Student Email']/following-sibling::td").text
    assert gender == browser.element("//td[text()='Gender']/following-sibling::td").text
    assert mobile == browser.element("//td[text()='Mobile']/following-sibling::td").text
    time.sleep(3)
