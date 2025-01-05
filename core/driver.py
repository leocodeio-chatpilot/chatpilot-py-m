# from selenium import webdriver
from contextlib import contextmanager
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options

from langchain_community.document_loaders import WebBaseLoader

class WebDriverManager:
    @staticmethod
    @contextmanager
    def get_driver():
        # chrome_options = Options()
        # chrome_options.add_argument('--headless') 
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        
        # service = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=service, options=chrome_options)
        print("HELLO",WebBaseLoader)
        # return WebBaseLoader
        yield WebBaseLoader
        # try:
        #     driver.implicitly_wait(10)
        #     yield driver
        # finally:
        #     driver.quit() 