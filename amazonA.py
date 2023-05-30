from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree
import time
import csv

driver = webdriver.Edge()
text = driver.page_source
html = etree.HTML(text)
all_list = []
def search(keywords):
    driver.get('https://www.amazon.com/')
    change_address('20001')
    inputtag = driver.find_element(By.ID,'twotabsearchtextbox')
    inputtag.send_keys(keywords)
    inputtag.send_keys(Keys.ENTER)

def change_address(postal):
    while True:
        try:
            driver.find_element(By.ID,'glow-ingress-line1').click()
            # driver.find_element(By.ID,'nav-global-location-slot').click()
            time.sleep(2)
        except Exception as e:
            driver.refresh()
            time.sleep(10)
            continue
        try:
            driver.find_element(By.ID,"GLUXChangePostalCodeLink").click()
            time.sleep(2)
        except:
            pass
        try:
            driver.find_element(By.ID,'GLUXZipUpdateInput').send_keys(postal)
            time.sleep(1)
            break
        except Exception as NoSuchElementException:
            try:
                driver.find_element(By.ID,'GLUXZipUpdateInput_0').send_keys(postal.split('-')[0])
                time.sleep(1)
                driver.find_element(By.ID,'GLUXZipUpdateInput_1').send_keys(postal.split('-')[1])
                time.sleep(1)
                break
            except Exception as NoSuchElementException:
                driver.refresh()
                time.sleep(10)
                continue
        print("重新选择地址")
    driver.find_element(By.ID,'GLUXZipUpdate').click()
    time.sleep(1)
    driver.refresh()
    time.sleep(3)

def review():
    result = driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]//div/div/span/span[4]').text
    a = int(result)
    a = a-1
    for i in range(a):
        urls = html.xpath('//a[@class="a-link-normal s-no-outline"]/@href')
        title = html.xpath('.//a[@target="_blank"]/span[@dir="auto"]/text()')
        pingfen = html.xpath('//span[@class="a-icon-alt"]/text()')
        rating_value = html.xpath('//span[@class="a-size-base"]/text()')
        price = html.xpath('//span[@class="a-offscreen"]/text()')
        for i in range(0, len(urls)):
            try:
                print(title[i], pingfen[i], rating_value[i], urls[i], price[i])
                list = [title[i], pingfen[i], rating_value[i], urls[i], price[i]]
                all_list.append(list)
            except Exception as e:
                pass
        headers = ["标题", '评分', '评论数', '链接', '价格']
        with open('amazon.csv', 'w', newline='', encoding='utf-8') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
            f_csv.writerows(all_list)
        forward = driver.find_element(By.XPATH, '(//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]//div/div/span/a)[last()]')
        forward.click()
        time.sleep(5)

if __name__ == '__main__':
    search('Bear glasses')
    review()
