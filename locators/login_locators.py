from selenium.webdriver.common.by import By


class LoginLocators:

    # ---------- LOGIN PAGE ELEMENTS ----------
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")