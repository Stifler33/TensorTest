import pytest
from selenium import webdriver
#import logging


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# @pytest.fixture(scope="session")
# def logger():
#     logging.basicConfig(level=logging.INFO, filename="test_1_log.log", filemode='w')
#     return logging
