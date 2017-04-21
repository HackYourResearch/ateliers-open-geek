#!usr/bin/env python2

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# browser = webdriver.Chrome(executable_path="/home/c24b/Téléchargements/opt/chromedriver",chrome_options=options)
def search_on_giphy(url="http://giphy.com/", query="meme"):
    browser = webdriver.PhantomJs()
    browser.get(url)
    element = driver.find_element_by_name("q")
    element.send_keys(query)

if __name__ == "__main__":
    search_on_giphy()
