# Сделайте функцию, которая будет печатать читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
def print_name_function(function_name, *args):
    name_func = function_name.__name__.split("_")
    for i in range((len(name_func))):
        print(name_func[i].title(), end=" ")
    print();
    for arg in args:
        print(arg.title())

def open_browser(browser_name):
    print("=" * 10, "Start", "=" * 10)
    print_name_function(open_browser, browser_name)
    print("=" * 10, "End", "=" * 10)

def go_to_companyname_homepage(page_url):
    print("=" * 10, "Start", "=" * 10)
    print_name_function(go_to_companyname_homepage, page_url)
    print("=" * 10, "End", "=" * 10)

def find_registration_button_on_login_page(page_url, button_text):
    print("=" * 10, "Start", "=" * 10)
    print_name_function(find_registration_button_on_login_page, page_url, button_text)
    print("=" * 10, "End", "=" * 10)

open_browser("chrome")
go_to_companyname_homepage("url")
find_registration_button_on_login_page("url", "button")