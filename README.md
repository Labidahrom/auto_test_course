# Тестирование сайта Makmen.ru с помощью Selenium WebDriver и Python
В данном репозитории находятся тесты написанные на языке Python для Selenium Webdriver с использованием фреймворка Pytest. Тесты проверяют функционал сайта makmen.ru, который может быть задействован в рамках типичного пользовательского сценария (формы обратной связи, корзину, сортировку карточек товара и другие элементы).

# Структура тестов и описание модулей
Для создания тестов была использована модель **Page Object**. Это означает что методы тестов группируются по классам в зависимости от типов страниц, к которым они относятся, а сами действия по тестированию веб приложения отделены от их реализации в коде. Для большей наглядности можно привести структуру файлов теста: 
1. **Наборы тест - кейсов (тест сьюты).** Тест кейсы объединены в наборы исходя из того, какие страницы сайта они тестируют: главная, страница каталога или карточка товара. Каждый тест кейс из набора - это последовательность каких то шагов, осуществление которых должно привести к определенному ожидаемому результату. Одному шагу пользователя всегда соответствует один метод. Пример такого тест кейса из набора - проверка возможности переключить город в шапке сайта. Всего есть 3 файла с наборами:
* *test_main_page.py* - наборы тестов главной страницы
* *test_catalog_page.py* - наборы тестов страницы каталога
* *test_product_page.py* - наборы тестов продуктовой страницы
2. **Файлы с кодом методов из тест кейсов (то есть где эти методы реализованы)**. Как и наборы тест кейсов, методы группируются по классам исходя из их принадлежности определенным страницам сайта. К этой группе относятся 4 файла:
* *main_page.py* - методы главной страницы
* *catalog_page.py* - методы страницы каталога
* *product_page.py* - методы продуктовой страницы
* *cart_page.py* - методы страницы корзины
3. **Различные вспомогательные файлы**:
* *base_page.py* - здесь описан базовый класс с методами, которые используют все остальные дочерние классы теста
* *locators.py* - здесь селекторы для всех тестов
* *conftest.py* - фикстуры и параметры Pytest
* *pytest.ini* - описания маркеров тестов для Pytest

# Пример реализации тест - кейса
Для наглядности можно разобрать тест-кейс `test_should_be_right_location` из набора тест - кейсов главной страницы (*test_main_page.py*). Тест проверяет правильность определения геопозиции пользователя сайта:

    def test_should_be_right_location(browser):
        page = MainPage(browser)  # создаем объект класса MainPage чтобы получить доступ ко всем методам главной страницы
        page.open("https://makmen.ru")  # открыть сайт
        page.click_on_accept_city_in_popup_massage()  # кликнуть по кнопке "Принять город"
        page.should_be_current_user_city_in_header("Санкт-Петербург")  # Проверка ожидаемого результата

Как видно, каждый шаг в тест кейсе представляет собой отдельный метод, по названию которого можно понять какое действие пользователя он реализует. Код методов этого тест-кейса описан в файле *MainPage.py*, передача метода происходит при инициализации объекта Page. Для проверки ожидаемого результата используется функция с названием `should_be_current_user_city_in_header("Санкт-Петербург")`, которая реализована в виде проверки ожидаемого значения названия города пользователя (его мы передаем как параметр функции) с фактическим.
 
Далее разберем один из методов приведенного выше тест кейса: click_on_accept_city_in_popup_massage(). Метод реализует клик пользователя по кнопке подтверждения выбора города, в коде же это выглядит как присваивание переменной элементу кнопки и далее передачи клика по ней:

    def click_on_accept_city_in_popup_massage(self):
        button = self.browser.find_element(*MainPageLocators.CITY_POPUP_YES_BUTTON)  # найти элемент
        button.click()  # кликнуть по элементу

В свою очередь элемент `*MainPageLocators.CITY_POPUP_YES_BUTTON` импортирован из модуля *locators.py*, и реализован через поиск элемента по CSS селектору:
`CITY_POPUP_YES_BUTTON = (By.CSS_SELECTOR, "input.prmn-cmngr__confirm-btn.btn-primary")`

Такая структура упрощает поддержку тестов в работоспособном состоянии, поскольку:
1. Дает возможность составлять разные тест кейсы без внесения изменений в код функций. Когда каждый шаг пользователя описан как отдельная функция, очень легко составлять новые тест кейсы просто собирая их из готовых методов как конструктор. Например мы легко можем сделать большой негативный набор тестов формы обратной связи, просто убрав из него часть шагов по заполнению полей или передав в них невалидные значения
2. Достаточно легкое изменение кода самих функций, поскольку локаторы элементов также вынесены в отдельных модуль. Если меняется CSS идентификатор самого элемента, мы редактируем код этого идентификатора в отдельном файле, не трогая код самой функции. Точно так если нам нужно поменять что то в тестовом окружении (например вместо браузера Chrome провести тесты в Firefox), нам не нужно менять код функций, а нужно лишь поменять драйвер браузера в файле *conftest.py*.
 
# Требования к тестовому окружению и способы запуска тестов
## Требования к тестовому окружению
Ниже приведен список приложений необходимых для работы данного набора тестов:
* ОС Windows
* Python (не ниже версии 3.0)
* Selenium WebDriver
* Pytest
* Google Chrome
* драйвер браузера Google Chrome ChromeDriver

## Запуск тестов
Запуск тестов производиться из командной строки. Всего для запуска есть 3 файла с наборами тест кейсов:
* *test_main_page.py*
* *test_catalog_page.py*
* *test_product_page.py*

При запуске необходимо указывать тесты какой версии сайта (мобильной или пк) при помощи передачи параметра в командную строку. Запуск ПК версии тестов производиться сочетанием:
pytest -m pc test_main_page.py - будут запущены все тесты ПК версии сайта для главной страницы
При запуске мобильных тестов, помимо основной маркировки также необходимо указать размер экрана:
pytest -m mobile –screen=mobile test_main_page.py - будут запущены все тесты мобильной версии для главной страницы

