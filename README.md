# Web Scrapping
R&amp;D project on Web Scrapping

## Used Technology
- Python
- Selenium

## Installation

### 1. Install Chrome Driver
We need chrome driver to work with selenium
- Check google Chrome version that is installed in your machine
```commandline
    google-chrome --version
```
- Install associated chromedriver. For more please visit [here](https://sites.google.com/chromium.org/driver/)
- Then run the following commands
```commandline
    wget https://chromedriver.storage.googleapis.com/99.0.4844.51/chromedriver_linux64.zip # 99.0.4844.51 is the supported version 
    unzip chromedriver_linux64.zip
    sudo mv chromedriver /usr/bin/chromedriver
    sudo chown root:root /usr/bin/chromedriver
    sudo chmod +x /usr/bin/chromedriver
```
- Finally check the installed chromedriver version
```commandline
    chromedriver --version 
```

### 2. Install other requirements
```commandline
    pip install -r requirements.txt
```

### Finally, run the project
```commandline
python scrapper.py
```
