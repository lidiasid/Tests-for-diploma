import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

CHROMEDRIVER_PATH = "C:\\Users\\lida1\\Desktop\\Diploma Tests\\Tests\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

class TestLifehackerSearch(unittest.TestCase):

    def setUp(self):
        service = Service(CHROMEDRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://lifehacker.ru/")

    def tearDown(self):
        self.driver.quit()

    def search(self, query):
        driver = self.driver

        search_icon = driver.find_element(By.CSS_SELECTOR, "#top-header-container > div > div > div.top-header__right > div.top-header__icon.top-header__icon-search > svg")
        search_icon.click()

        search_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#top-header-container > div > div > div > input"))
        )
        search_box.send_keys(query + Keys.RETURN)

    def test_search_functionality(self):
        self.search("технологии")

        active_tab = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#main > div > section > div > div.search-window__top-items > div.search-window__tabs > div.search-tabs > span.search-tabs__tab.search-tabs__tab--active"))
        )
        self.assertEqual(active_tab.text, "Все материалы", f'Expected "Все материалы", but got {active_tab.text}')

if __name__ == "__main__":
    unittest.main()
