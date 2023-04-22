from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()
def search(keywords):
    driver.get('https://www.amazon.cn/')
    inputtag = driver.find_element(By.ID,'twotabsearchtextbox')
    inputtag.send_keys(keywords)
    inputtag.send_keys(Keys.ENTER)

def review():
    result = driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]//span/span[4]').text
    a = int(result)
    a = a-1
    for i in range(a):
        h2s = driver.find_elements(By.XPATH, '//*[@id="search"]//ancestor::h2')
        time.sleep(2)
        for h2 in h2s:
            print(h2.find_element(By.CSS_SELECTOR, "span").text)
            print(h2.find_element(By.XPATH, '//*[@id="search"]//div/a/span[1]').text)
        forward = driver.find_element(By.XPATH, '(//*[@id="search"]//div/div/span/a)[last()]')
        forward.click()
        time.sleep(2)


if __name__ == '__main__':
    search('Bear glasses')
    review()
