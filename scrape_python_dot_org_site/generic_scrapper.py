import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from scrapper import BaseScrapper


class Scrapper(BaseScrapper):
    def scrape(self):
        url = "http://www.python.org"
        self.driver.get(url=url)

        # confirm that title has the word “Python” in it
        assert "Python" in self.driver.title

        search = self.driver.find_element(By.NAME, "q")
        search.clear() # clear any pre-populated text in the input field (e.g. “Search”) so it doesn’t affect search results

        search.send_keys("pycon")
        search.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source

        time.sleep(5)
        self.quite_driver()


if __name__ == '__main__':
    Scrapper().scrape()
