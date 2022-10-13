from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

FORM_URL = "https://forms.gle/ohMobyWhkBZtWpii6"


class Form:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(FORM_URL)

    def add_address(self, address):
        self.driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
            address)

    def add_price(self, price):
        self.driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
            price)

    def add_link(self, link):
        self.driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
            link)

    def submit(self):
        self.driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
        self.driver.refresh()

    def driver_quit(self):
        self.driver.quit()
