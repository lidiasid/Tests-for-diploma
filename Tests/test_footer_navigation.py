import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class TestLifehackerNavigation(unittest.TestCase):

    def setUp(self):
        service = Service("C:\\Users\\lida1\\Desktop\\Diploma Tests\\Tests\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)

    def test_footer_links(self):
        driver = self.driver
        driver.get('https://lifehacker.ru')

        # Получение всех ссылок в футере
        footer_links = driver.find_elements(By.CSS_SELECTOR, "footer a")

        for link in footer_links:
            main_window = driver.current_window_handle  # Запомнить текущее окно
            href = link.get_attribute('href')  # Получение URL ссылки
            link.click()

            # Переключиться на новое окно, если оно открыто
            new_window = None
            for handle in driver.window_handles:
                if handle != main_window:
                    new_window = handle
                    break

            if new_window:
                driver.switch_to.window(new_window)

            # Ожидание перехода на новую страницу (проверка URL)
            try:
                WebDriverWait(driver, 10).until(EC.url_to_be(href))
            except TimeoutException:
                print(f"Failed to navigate to {href}")

            # Возвращение назад к футеру
            if new_window:
                driver.close()  # Закрыть новое окно
                driver.switch_to.window(main_window)  # Вернуться к основному окну
            else:
                driver.back()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
