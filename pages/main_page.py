import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    cookie = (By.ID, "rcc-confirm-button")
    order_button_top = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    order_button_bottom = (
    By.XPATH, "//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Заказать']")
    faq_questions = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemButton']")
    faq_answers = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemPanel']")
    scooter_logo = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    yandex_logo = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    @allure.step('Принимаем куки')
    def accept_cookies(self):
        self.click_element(self.cookie)

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_order_button(self, button_type):
        if button_type == "top":
            self.click_element(self.order_button_top)
        else:
            self.scroll_to_element(self.order_button_bottom)
            self.click_element(self.order_button_bottom)


    @allure.step('Проверяем ответ на вопрос в FAQ')
    def get_faq_answer_text(self, question_index):
        faq_section = self.find_element((By.ID, "accordion__heading-0"))
        self.driver.execute_script("arguments[0].scrollIntoView();", faq_section)
        questions = self.find_elements(self.faq_questions)
        questions[question_index].click()
        answer_locator = (By.ID, f"accordion__panel-{question_index}")
        return self.find_element(answer_locator).text

    @allure.step('Нажимаем на лого "Самокат"')
    def click_scooter_logo(self):
        self.click_element(self.scooter_logo)

    @allure.step('Нажимаем на лого "Яндекс"')
    def click_yandex_logo(self):
        self.click_element(self.yandex_logo)