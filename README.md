# Web Scrapping
R&amp;D project on Web Scrapping

## Used Technology
- Python 3.10+
- Selenium 4.26.1+

## Installation
### 1. Install the dependencies
Traditionally, Selenium requires a WebDriver and a browser (like Chrome) to automate web interactions. However, 
with Selenium 4.10 and above, you can bypass the need for a WebDriver in certain scenarios. This allows for more 
flexible and efficient automation.
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
```
This approach eliminates the need for a separate WebDriver. Selenium handles the browser interaction internally.

### 2. Install other requirements
```commandline
    pip install -r requirements.txt
```
