from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from core.driver import WebDriverManager

class BaseScraper(ABC):
    def __init__(self, url: str, api_key: str):
        self.url = url
        self.api_key = api_key
        
    @abstractmethod
    def scrape(self):
        pass
    
    def get_page_content(self):
        # with WebDriverManager.get_driver() as driver:
        #     driver.get(self.url)
        #     soup = BeautifulSoup(driver.page_source, "html.parser")
        #     return soup
        web_loader = WebDriverManager.get_driver().__enter__()
        print("debug log 1 - base.py - get_page_content - web_loader", web_loader)
        docs = web_loader(self.url)
        print("debug log 1 - base.py - get_page_content - docs", docs)
        soup = docs.load().pop().page_content
        return soup
