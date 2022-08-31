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

selene_name = "yashaka/selene: User-oriented Web UI browser tests in Python"


@pytest.fixture()
def open_browser():
    browser.config.browser_name = 'chrome'

@pytest.fixture()
def configure_mobile_browser(open_browser):
    browser.config.window_width = 375
    browser.config.window_height = 667

@pytest.fixture()
def configure_desktop_browser(open_browser):
    browser.config.window_width = 1920
    browser.config.window_height = 1080


def test_first_page_mobile_positive(configure_mobile_browser):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element("//div[text()='Practice Form']").should(have.text(name_form))
    browser.element("//input[@id = 'firstName']").type(first_name)
    browser.element("//input[@id = 'lastName']").type(last_name)
    browser.element("//input[@id = 'userEmail']").type(user_email)
    browser.element("//label[text() = '" + gender + "']").click()
    browser.element("//input[@id = 'userNumber']").type(mobile).press_enter()
    browser.element("//div[@id='example-modal-sizes-title-lg']").should(have.text(fill_in_form_title))
    browser.element("//td[text()='Student Name']/following-sibling::td").should(have.text(student_name))
    browser.element("//td[text()='Student Email']/following-sibling::td").should(have.text(user_email))
    browser.element("//td[text()='Gender']/following-sibling::td").should(have.text(gender))
    browser.element("//td[text()='Mobile']/following-sibling::td").should(have.text(mobile))
    time.sleep(3)

def test_first_page_desktop_positive(configure_desktop_browser): #TODO пределать под retern и возврат значений
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element("//div[text()='Practice Form']").should(have.text(name_form))
    browser.element("//input[@id = 'firstName']").type(first_name)
    browser.element("//input[@id = 'lastName']").type(last_name)
    browser.element("//input[@id = 'userEmail']").type(user_email)
    browser.element("//label[text() = '" + gender + "']").click()
    browser.element("//input[@id = 'userNumber']").type(mobile).press_enter()
    browser.element("//div[@id='example-modal-sizes-title-lg']").should(have.text(fill_in_form_title))
    browser.element("//td[text()='Student Name']/following-sibling::td").should(have.text(student_name))
    browser.element("//td[text()='Student Email']/following-sibling::td").should(have.text(user_email))
    browser.element("//td[text()='Gender']/following-sibling::td").should(have.text(gender))
    browser.element("//td[text()='Mobile']/following-sibling::td").should(have.text(mobile))
    time.sleep(1)


def test_second_page_mobile_positive(configure_mobile_browser):
    browser.open('https://google.com')
    browser.element('//input[@title="Поиск"]').should(be.blank).type('selene').press_enter()
    browser.element('//div[@id="search"]').should(have.text(selene_name))
def test_second_page_desktop_positive(configure_desktop_browser):
    browser.open('https://google.com')
    browser.element('//input[@title="Поиск"]').should(be.blank).type('selene').press_enter()
    browser.element('//div[@id="search"]').should(have.text(selene_name))

def test_first_page_desktop_negative(configure_desktop_browser):
    browser.open('https://google.com')
    browser.element('//input[@title="Поиск"]').should(be.blank).type('selene1111').press_enter()
    browser.element('//div[@id="search"]').should(have.no.text(selene_name))
