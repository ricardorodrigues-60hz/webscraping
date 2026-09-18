from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Google:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://google.com.br'
        self.search_bar = 'ti6dpd'# id
        self.btn_search = 'btnK' # name
        self.btn_lucky = 'btnI' # name

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):
        self.driver.find_element(By.ID, self.search_bar).send_keys(word)
        button = self.driver.find_element(By.NAME, self.btn_search)
        button.click()

    def lucky(self, word='None'):
        self.driver.find_element(By.ID, self.search_bar).send_keys(word)
        self.driver.find_element(By.NAME, self.btn_lucky).click()
        
g = Google()
g.navigate()
g.search('Live de Python')