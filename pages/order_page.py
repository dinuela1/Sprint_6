import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    # Шаг 1
    name_input = (By.XPATH, "//input[@placeholder='* Имя']")
    last_name_input = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_input = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_input = (By.CSS_SELECTOR, ".select-search__input")
    metro_option = (By.XPATH, "//div[contains(@class, 'Order_Text__2broi') and text()='{}']")
    phone_input = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[text()='Далее']")

    # Шаг 2
    date_input = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rental_period = (By.CSS_SELECTOR, ".Dropdown-placeholder")
    rental_option = (By.XPATH, "//div[text()='{}']")
    color_checkbox = (By.ID, "{}")
    comment_input = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    confirm_button = (By.XPATH, "//button[text()='Да']")
    success_window = (By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ")

    @allure.step('Заполняем 1/2 часть анкеты на заказ самоката')
    def fill_step1(self, name, last_name, address, metro, phone):
        self.send_keys(self.name_input, name)
        self.send_keys(self.last_name_input, last_name)
        self.send_keys(self.address_input, address)
        self.click_element(self.metro_input)
        self.send_keys(self.metro_input, metro.split()[0])
        metro_locator = (self.metro_option[0], self.metro_option[1].format(metro))
        metro_option = self.wait_until_clickable(metro_locator, timeout=15)
        metro_option.click()
        self.send_keys(self.phone_input, phone)
        self.scroll_to_element(self.next_button)
        self.click_element(self.next_button)

    @allure.step('Заполняем 2/2 часть анкеты на заказ самоката')
    def fill_step2(self, date, period, color, comment):
        # Установка даты
        date_field = self.find_element(self.date_input)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ENTER)
        self.click_element(self.rental_period)
        period_locator = (self.rental_option[0], self.rental_option[1].format(period))
        period_option = self.wait_until_clickable(period_locator)
        period_option.click()
        color_locator = (self.color_checkbox[0], self.color_checkbox[1].format(color))
        self.click_element(color_locator)
        self.send_keys(self.comment_input, comment)
        self.scroll_to_element(self.order_button)
        order_button = self.wait_until_clickable(self.order_button)
        self.action_click(order_button)
        confirm_button = self.wait_until_clickable(self.confirm_button, timeout=20)
        confirm_button.click()

    @allure.step('Дожидаемся появления окна с подтверждением заказа')
    def is_success_displayed(self):
        return self.is_element_displayed(self.success_window, timeout=20)