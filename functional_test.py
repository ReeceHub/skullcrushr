from selenium import webdriver
import unittest

class TestNewVisitor(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_page_loads(self):
        self.driver.get('http://localhost:8000')

        self.assertIn('Django', self.driver.title)

if __name__ == '__main__':
    unittest.main()
