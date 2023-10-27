from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
import time
import os

class TestWebsiteAdaptivity(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://lifehacker.ru/")
        
        # Создание папки для скриншотов, если ее нет
        self.screenshot_folder = "C:\\Users\\lida1\\Desktop\\Diploma Tests\\Tests\\Screenshots"
        if not os.path.exists(self.screenshot_folder):
            os.makedirs(self.screenshot_folder)

    def test_resolutions(self):
        # Добавлены разрешения для некоторых популярных мобильных устройств
        resolutions = [
            (1280, 800), (1366, 768), (1920, 1080),
            (1440, 900), (1600, 900), (1024, 768),
            (800, 600), (1680, 1050),
            (375, 667),  # iPhone 6/7/8
            (414, 736),  # iPhone 6/7/8 Plus
            (375, 812),  # iPhone X/XS/11 Pro
            (414, 896),  # iPhone XR/11/XS Max
            (360, 640),  # Most Android devices
            (320, 568)   # iPhone 5
        ]
        
        for width, height in resolutions:
            with self.subTest(f"Testing {width}x{height}"):
                self.driver.set_window_size(width, height)
                time.sleep(2)  # Дать время для загрузки страницы
                screenshot_path = os.path.join(self.screenshot_folder, f"{width}x{height}.png")
                self.driver.save_screenshot(screenshot_path)
                
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

