import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setUp(request):
    logging.info("Tests will run in Chrome")
    chr_options = webdriver.ChromeOptions()
    chr_options.add_experimental_option("detach", True)
    chr_options.add_argument('--disable-notifications')
    chr_options.add_argument('--start-maximized')  # for windows
    chr_options.add_argument('--kiosk')  # for mac
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chr_options)
    driver.get("https://www.amazon.com.tr/")
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield  # tearDown
    driver.quit()



