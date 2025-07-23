from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"
        self.default_timeout = 15

    @allure.step("Открыть сайт")
    def go_to_site(self):
        self.driver.get(self.base_url)

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Найти элемент {locator} с ожиданием его видимости")
    def find_element(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        return self.wait_until_visible(*locator, timeout)

    @allure.step("Найти элементы {locator} с ожиданием их видимости")
    def find_elements(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_any_elements_located(locator)
            )
        except TimeoutException:
            return []

    @allure.step("Кликнуть на элемент: {locator}")
    def click_element(self, locator, timeout=None):
        element = self.wait_until_clickable(locator, timeout)
        element.click()

    @allure.step("Ввести текст '{text}' в элемент: {locator}")
    def send_keys(self, locator, text, timeout=None):
        element = self.wait_until_visible(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Ожидать видимости элемента: {locator}")
    def wait_until_visible(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидать кликабельности элемента: {locator}")
    def wait_until_clickable(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ожидать присутствия элемента в DOM: {locator}")
    def wait_until_present(self, locator, timeout=None):
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Прокрутить к элементу: {locator}")
    def scroll_to_element(self, locator, timeout=None):
        element = self.wait_until_present(locator, timeout)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return element

    @allure.step("Нажать Enter в элементе: {locator}")
    def press_enter(self, locator, timeout=None):
        element = self.wait_until_visible(locator, timeout)
        element.send_keys(Keys.ENTER)

    @allure.step("Проверить видимость элемента: {locator}")
    def is_element_displayed(self, locator, timeout=None):
        try:
            return self.wait_until_visible(locator, timeout).is_displayed()
        except TimeoutException:
            return False

    #@allure.step("Переключиться на окно #{index}")
    #def switch_to_window(self, index=0):
     #   WebDriverWait(self.driver, self.default_timeout).until(
      #      lambda d: len(d.window_handles) > index
       # )
        #self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step("Ожидать текст '{text}' в URL")
    def wait_for_url_contains(self, text, timeout=None):
        timeout = timeout or self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text),
            message=f"URL doesn't contain '{text}'"
        )

    @allure.step("Кликнуть ActionChains на элемент")
    def action_click(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step("Пролистать блок FAQ для проверки всех вопросов")
    def execute_script_faq(self, "text", faq_element):
        return self.driver.execute_script("text", faq_element)
