import time

import pytest
from selene import have, be, by, command
from selene.support.shared import browser

from learning.tests.utils.files import abs_path_from_project_root


def test_submit_user_details():
    browser.open('/text-box')
    ####удаление одного конкретного элемента
    ads = browser.all('#RightSide_Advertisement')
    ads.should(have.size_greater_than_or_equal(1))
    # Если реклама то есть то нет то можно настроить такой вариант
    # if ads.wait_until(have.size_greater_than_or_equal(1)) так как until не падает а возвращает false или через matching. Until ждет а matching нет
    # if ads.matching(have.size_greater_than_or_equal(1))
    # блок который нужно удалить
    # ads[0]._execute_script('element.remove()')  # удаляет элемент по номеру
    ads.perform(command.js.remove)  # удаляет все элементы ads[0] можно так тоже
    ####удаление нскольких элементов
    # browser.all('#RightSide_Advertisement').should(have.size_greater_than_or_equal(1)) # ждет чтобы все отобоазилось, одна реклама
    # browser.execute_script('document.querySelectorAll("#RightSide_Advertisement").forEach(element => element.remove())')  # как убрать несколько элементов через джаваскрипт
    browser.should(have.title('ToolsQA'))
    browser.with_(timeout=6).element('.main-header').should(
        have.text('Text Box'))  # например можно так таймаут установить эмулируя медленный браузер
    browser.element(by.text('Text Box')).should(be.visible)  # поиск что такой текст есть
    browser.with_(timeout=6).element('.main-header').should(
        be.visible)  # вместо поиска по тексту который является часьтью UI лучше использовать такую? но если мы самми вводим текст и его потом ищем то ок
    # browser.all('#userForm input, #userForm textarea').with_(timeout=3).should(have.size(4)) # например можно так таймаут установить эмулируя долгую загрузку элементов
    browser.element('#userForm').all('input, textarea').with_(timeout=3).should(
        have.size(4))  # лучше так искать несколько сложных элементов
    browser.all('.form-label').filtered_by(have.text("Address"))[1].should(
        have.text('Permanent Address'))  # Filtered фильтрует элемент берет 2-ой и справнивает его
    browser.element('#userName').type('Ivan')
    browser.element('#userEmail').type('Ivanov@maad.tu')
    browser.element('#currentAddress').type('Current google-chrome version is 105.0.5195')
    browser.element('#permanentAddress').type('Get LATEST chromedriver version for 105.0.5195 google-chrome')
    browser.element('#submit').click()
    # browser.element('#submit').perform(command.js.click)  # если не кликается например сттандартными средствами то можно через js или очистить форму
    # submit = browser.element('#submit').with_(click_by_js=True) # кнопка всегда будт кликаться джаваскриптом
    # submit.click()
    # TODO browser.element('#uploadFile').send_keys(abs_path_from_project_root('resources/test.txt'))
    browser.all('#output p').should(have.texts('Ivan', 'Ivanov@maad.tu', 'Current google-chrome version is 105.0.5195',
                                               'Get LATEST chromedriver version for 105.0.5195 google-chrome'))
    time.sleep(1)
