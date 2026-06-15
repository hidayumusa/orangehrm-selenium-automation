import pytest  # import pytest framework untuk create fixture

from selenium import webdriver  # import Selenium WebDriver
from selenium.webdriver.chrome.service import Service  # Chrome service setup
from webdriver_manager.chrome import ChromeDriverManager  # auto install ChromeDriver


@pytest.fixture  # fixture = reusable setup untuk test
def driver():

    options = webdriver.ChromeOptions()  # set Chrome options (browser config)
    options.add_argument("--no-sandbox")  # disable sandbox (stability)
    options.add_argument("--disable-dev-shm-usage")  # fix memory issue

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),  # auto download & setup driver
        options=options  # apply browser options
    )

    driver.maximize_window()  # maximize browser window
    yield driver  # pass driver ke test case
    driver.quit()  # close browser after test selesai