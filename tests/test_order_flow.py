import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

order_data = [
    {
        "button": "top",
        "name": "Иван",
        "last_name": "Иванов",
        "address": "Красная площадь, 1",
        "metro": "Сокольники",
        "phone": "88005553535",
        "date": "01.01.2025",
        "period": "сутки",
        "color": "black",
        "comment": "Первый заказ"
    },
    {
        "button": "bottom",
        "name": "Мария",
        "last_name": "Петрова",
        "address": "Невский проспект, 10",
        "metro": "Сокольники",
        "phone": "88005553536",
        "date": "10.01.2025",
        "period": "двое суток",
        "color": "grey",
        "comment": "Второй заказ"
    }
]


class TestOrderFlow:
    @pytest.mark.parametrize("data", order_data)
    @allure.title('Проверка позитивного сценария всего флоу заказа')
    def test_successful_order(self, driver, data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.go_to_site()
        main_page.accept_cookies()
        main_page.click_order_button(data["button"])

        order_page.fill_step1(
            data["name"],
            data["last_name"],
            data["address"],
            data["metro"],
            data["phone"]
        )

        order_page.fill_step2(
            data["date"],
            data["period"],
            data["color"],
            data["comment"]
        )

        assert order_page.is_success_displayed(), "Окно оформления заказа не отображается"
