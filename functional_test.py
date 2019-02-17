import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.close()
    driver.quit()

def test_page_loads(driver):
    driver.get('http://localhost:8000')
    assert 'Django' in driver.title
