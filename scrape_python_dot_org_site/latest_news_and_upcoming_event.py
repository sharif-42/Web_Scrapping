from selenium.webdriver.common.by import By
from scrapper import BaseScrapper


class ScrapePythonOrgPage(BaseScrapper):

    def get_url(self):
        return "http://www.python.org"

    def get_latest_news(self):
        latest_news_list = []

        news_items = self.driver.find_elements(By.CSS_SELECTOR, ".medium-widget.blog-widget ul.menu li")
        # Extract data
        for item in news_items:
            # Extract datetime
            date_element = item.find_element(By.TAG_NAME, "time")
            datetime_value = date_element.get_attribute("datetime")

            # Extract the link and text
            link_element = item.find_element(By.TAG_NAME, "a")
            link_href = link_element.get_attribute("href")
            link_text = link_element.text

            latest_news_list.append({
                "datetime": datetime_value.split("T")[0],
                "link": link_href,
                "line_text": link_text,
            })
            # print(f"Date: {datetime_value}")
            # print(f"Link: {link_href}")
            # print(f"Text: {link_text}")
            # print("-" * 40)
        return latest_news_list

    def get_upcoming_events(self):
        upcoming_event_list = []
        upcoming_events = self.driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last ul.menu li")
        # Extract data
        for item in upcoming_events:
            # Extract datetime
            date_element = item.find_element(By.TAG_NAME, "time")
            datetime_value = date_element.get_attribute("datetime")

            # Extract the link and text
            link_element = item.find_element(By.TAG_NAME, "a")
            link_href = link_element.get_attribute("href")
            link_text = link_element.text

            upcoming_event_list.append({
                "datetime": datetime_value.split("T")[0],
                "link": link_href,
                "line_text": link_text,
            })
            # print(upcoming_event_list)
            # print(f"Date: {datetime_value}")
            # print(f"Link: {link_href}")
            # print(f"Text: {link_text}")
            # print("-" * 40)
        return upcoming_event_list

    def scrape(self):
        self.driver.get(url=self.get_url())

        # confirm that title has the word “Python” in it
        latest_news = self.get_latest_news()
        upcoming_event = self.get_upcoming_events()

        self.quite_driver()

if __name__ == '__main__':
    ScrapePythonOrgPage().scrape()