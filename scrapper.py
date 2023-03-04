from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Scrapper:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def close_driver(self):
        # close will close one tab, if just one tab was open, by default most browsers will exit entirely.
        self.driver.close()

    def quite_driver(self):
        # The quit method will exit the browser whereas close will close one tab,
        # but if just one tab was open, by default most browsers will exit entirely.
        self.driver.quit()

    def scrape(self):
        url = "http://www.python.org"
        self.driver.get(url=url)

        # confirm that title has the word “Python” in it
        assert "Python" in self.driver.title

        elem = self.driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source

        self.quite_driver()


if __name__ == '__main__':
    Scrapper().scrape()
