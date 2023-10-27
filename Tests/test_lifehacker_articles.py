from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.webdriver.chrome.service import Service

# Настройка логгера для сохранения результатов в файл
logging.basicConfig(filename='lifehacker_articles.log', level=logging.DEBUG, encoding='utf-8')

class LifeHackerScraper:
    def __init__(self, driver_path):
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service)
        logging.debug("Driver initialized")

    def fetch_articles(self, url):
        try:
            self.driver.get(url)
            logging.debug(f"Открыт URL: {url}")

            articles = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-jest='title']"))
            )

            logging.debug(f"Найдено {len(articles)} статей")
            return articles
        except Exception as e:
            logging.error(f"Ошибка при получении статей: {e}")
            return []
    
    def save_article_titles_to_log(self, articles):
        for index, article in enumerate(articles):
            try:
                title = article.text
                logging.debug(f"Статья #{index + 1}. Заголовок: {title}")
            except Exception as e:
                logging.error(f"У статьи #{index + 1} нет заголовка: {e}")
    
    def close(self):
        self.driver.quit()
        logging.debug("Драйвер закрыт")


if __name__ == "__main__":
    logging.debug("Начало скрипта")
    scraper = LifeHackerScraper(driver_path="C:\\Users\\lida1\\Desktop\\Diploma Tests\\Tests\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    
    articles = scraper.fetch_articles("https://lifehacker.ru/")
    scraper.save_article_titles_to_log(articles)
    
    scraper.close()
    logging.debug("Конец скрипта")
