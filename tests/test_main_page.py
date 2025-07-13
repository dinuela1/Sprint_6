import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


class TestMainPage:
    @pytest.mark.parametrize("question_index, expected_answer", [
        (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (1,
         "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (2,
         "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (3, "Вы можете оплатить курьеру наличными или картой. Также возможна оплата картой онлайн."),
        (4,
         "Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру."),
        (5, "Да, вы можете отменить заказ в любое время до его получения. Штрафа не будет."),
        (6, "Да, обязательно. Мы предоставляем шлемы всем нашим клиентам."),
        (7, "Вы можете сделать заказ через мобильное приложение или на сайте.")
    ])
    @allure.title('Вопросы о важном: Проверка соответствия ответов на вопросы')
    def test_faq_answers(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.accept_cookies()
        answer_text = main_page.get_faq_answer_text(question_index)
        assert answer_text == expected_answer, f"Ожидался ответ: {expected_answer}"

    @allure.title('Проверка перехода на главную страницу Яндекс Самокат при нажатии на Самокат')
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_scooter_logo()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Проверка перехода на главную страницу Яндекс Дзен при нажатии на Яндекс')
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.accept_cookies()
        main_page.click_yandex_logo()
        WebDriverWait(driver, 30).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in driver.current_url
