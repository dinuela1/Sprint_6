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

    def fill_step1(self, name, last_name, address, metro, phone):
        self.find_element(self.name_input).send_keys(name)
        self.find_element(self.last_name_input).send_keys(last_name)
        self.find_element(self.address_input).send_keys(address)
        metro_field = self.find_element(self.metro_input)
        metro_field.click()
        metro_field.send_keys(metro.split()[0])
        metro_option_locator = (By.XPATH, f"//div[contains(text(), '{metro}')]")
        metro_option = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(metro_option_locator)
        )
        self.driver.execute_script("arguments[0].click();", metro_option)
        self.find_element(self.phone_input).send_keys(phone)
        next_btn = self.find_element(self.next_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", next_btn)
        next_btn.click()

    def fill_step2(self, date, period, color, comment):
        # Установка даты
        date_field = self.find_element(self.date_input)
        date_field.send_keys(date)
        self.find_element(self.rental_period).click()
        period_locator = (By.XPATH, f"//div[text()='{period}']")
        period_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(period_locator)
        )
        period_option.click()
        color_locator = (By.ID, color)
        self.find_element(color_locator).click()
        self.find_element(self.comment_input).send_keys(comment)
        order_btn = self.find_element(self.order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", order_btn)
        self.driver.execute_script("arguments[0].click();", order_btn)
        confirm_btn = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.confirm_button)
        )
        confirm_btn.click()

    def is_success_displayed(self):
        try:
            return WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.success_window)
            ).is_displayed()
        except:
            self.driver.save_screenshot("order_success_error.png")
            return False