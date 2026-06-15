from locators.login_locators import LoginLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def __init__(self, driver):
        self.driver = driver

    # ---------------- OPEN PAGE ----------------
    def open(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.USERNAME)
        )

    # ---------------- LOGIN ----------------
    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.USERNAME)
        ).send_keys(username)

        self.driver.find_element(*LoginLocators.PASSWORD).send_keys(password)
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    # ---------------- VALIDATION ----------------
    def is_logged_in(self):
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: "dashboard" in d.current_url.lower()
            )
            return True
        except TimeoutException:
            return False