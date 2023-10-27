import os
from selenium import webdriver
import unittest

class TestCrossBrowserAndAdaptivity(unittest.TestCase):
    
    def test_cross_browser_functionality(self):

        # Testing in Chrome
        try:
            os.environ["webdriver.chrome.driver"] = "C:\\Users\\lida1\\Desktop\\Diploma Tests\\Tests\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
            chrome_driver = webdriver.Chrome()
            chrome_driver.get("https://lifehacker.ru/")
            self.assertEqual(chrome_driver.current_url, "https://lifehacker.ru/")
            chrome_driver.quit()
        except Exception as e:
            print(f"Error in Chrome: {e}")

        # Testing in Firefox
        try:
            os.environ["webdriver.gecko.driver"] = "C:\\Users\\lida1\\Desktop\\Diploma Tests\\Tests\\geckodriver-v0.33.0-win64\\geckodriver.exe"
            firefox_driver = webdriver.Firefox()
            firefox_driver.get("https://lifehacker.ru/")
            self.assertEqual(firefox_driver.current_url, "https://lifehacker.ru/")
            firefox_driver.quit()
        except Exception as e:
            print(f"Error in Firefox: {e}")

if __name__ == "__main__":
    unittest.main()
