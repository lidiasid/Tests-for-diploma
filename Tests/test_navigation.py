import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class TestLifehackerNavigation(unittest.TestCase):

    def setUp(self):
        service = Service("C:\\Users\\lida1\\Desktop\\Diploma Tests\\Tests\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)

    def test_navigation_menu(self):
        driver = self.driver
        driver.get('https://lifehacker.ru')

        # Список элементов в навигационном меню
        menu_items = ['Лучшее', 'Рубрики', 'Рецепты', 'Промокоды', 'Подкасты', 'Сервисы', 'Колонки']

        for item in menu_items:
            try:
                # Ожидание появления элемента меню
                menu_item = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.LINK_TEXT, item))
                )
                # Сохранение текущего URL
                current_url = driver.current_url

                # Клик по элементу меню
                menu_item.click()

                # Ожидание изменения URL
                WebDriverWait(driver, 20).until(
                    lambda d: d.current_url != current_url
                )

                # Возвращение на главную страницу для следующей итерации
                driver.get('https://lifehacker.ru')

            except (NoSuchElementException, TimeoutException):
                self.fail(f'Menu item {item} not found')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



