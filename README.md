# qa_guru_python_2_2

## Homeworks - папка для домашек

## Learning - для повторения на уроках

### Python commands

pytest --fixtures -- список всех используемых фикстур

### Git commands 

ssh-keygen -t rsa  - создание ключевой пары для Ubuntu/MAc
ssh-keygen -t ed25519 -C "svmyhome@mail.ru" - windows

git init
git rm --cached nameFile 


## как назвать проекты в PyCharm
название проекта-test
например: demoqa-test 

## Selene
should - любая проверка  -- should(have.tite('name')) or be
element и all поиск по элементу/элементам
bowser.config.(разные настройки)
browser.config.timeout = 4   # к каждой команде применяется ожидание  4 секунды
    browser.with_(timeout=6).element('.main-header').should(have.text('Text Box'))  # например можно так таймаут установить эмулируя медленный браузер
    browser.all('#userForm input, #userForm textarea').with_(timeout=3).should(have.size(4)) # например можно так таймаут установить эмулируя долгую загрузку элементов
 