import pytest
from selenium import webdriver

@pytest.fixture
def init_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()