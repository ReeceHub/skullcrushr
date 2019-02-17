from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://localhost:8000')

def test_page_loads():
    assert 'Django' in driver.title
    driver.close()
