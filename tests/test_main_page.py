import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from data import *


class TestMainPage:
    @pytest.mark.parametrize("question_index, expected_answer", FAQ_index)
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
        assert main_page.get_current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Проверка перехода на главную страницу Яндекс Дзен при нажатии на Яндекс')
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.accept_cookies()
        main_page.click_yandex_logo()
        WebDriverWait(driver, 30).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in main_page.get_current_url
