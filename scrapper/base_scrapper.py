from abc import ABC, abstractmethod

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BaseScrapper(ABC):

    def __init__(self):
        service = Service()
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)

    def close_driver(self):
        # close will close one tab, if just one tab was open, by default most browsers will exit entirely.
        self.driver.close()

    def quite_driver(self):
        # The quit method will exit the browser whereas close will close one tab,
        # but if just one tab was open, by default most browsers will exit entirely.
        self.driver.quit()

    @abstractmethod
    def scrape(self):
        """Method that must be implemented by subclasses."""
        pass
