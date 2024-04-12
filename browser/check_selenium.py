# pip install webdriver-manager
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from browser.crome_options import setting_chrome_options


def open_page_with_selenium(url: str):
    service = Service(ChromeDriverManager().install())

    # Инициализируем драйвер с указанными опциями
    driver = webdriver.Chrome(service=service, options=setting_chrome_options())
    # Открываем страницу в браузере

    driver.get(url)
    time.sleep(15)

    return driver


if __name__ == '__main__':
    result = open_page_with_selenium('https://qui-quo.ru/ta-rating/FP00-FW86/item/0')
    print(result.title)
    print(result.current_url)
    # Закрываем браузер
    result.quit()
