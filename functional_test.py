from selenium import webdriver
import unittest

class TestNewVisitor(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_polls_page_loads(self):
        self.driver.get('http://localhost:8000/polls')

        self.assertIn('Hello, world.', self.driver.page_source)

if __name__ == '__main__':
    unittest.main()
