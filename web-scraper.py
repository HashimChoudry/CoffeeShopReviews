from bs4 import BeautifulSoup
import requests
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class coffeeShop:
    def __init__(self, name):
        self.name=name

driver=webdriver.Chrome()
cofeeShopArr =[]


filename = "data"
url = "https://www.google.co.uk/maps/search/coffee+shops+in+manchester/@53.4785683,-2.2489418,15z/data=!3m1!4b1?entry=ttu"
count = 0

driver.get(url)

try:
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Accept all']"))
    )
    button.click()
except:
    print("cookies page did not open")

action=ActionChains(driver)
shops = driver.find_elements(By.CLASS_NAME,'hfpxzc')

while len(shops) < 1000:
    print(len(shops))
    shopLen = len(shops)
    scroll_origin = ScrollOrigin.from_element(shops[len(shops) - 1])
    action.scroll_from_origin(scroll_origin, 0, 100).perform()
    time.sleep(2)
    shops = driver.find_elements(By.CLASS_NAME,'hfpxzc')

    if len(shops) == shopLen:
        shopLen +=1
        if shopLen >20:
            break
    else:
        shopLen=0

for i in range(len(shops)):
    scroll_origin=ScrollOrigin.from_element(shops[i])
    action.scroll_from_origin(scroll_origin, 0, 100).perform()
    action.move_to_element(shops[i]).perform()
    shops[i].click()
    time.sleep(2)
    source=driver.page_source
    try:
        soup=BeautifulSoup(source,'html.parser')
        name_html=soup.find('h1',{"class":"DUwDvf"}).text
        print(name_html)
        cofeeShopArr.append(coffeeShop(name_html))
    except:
        print("error")
driver.quit()

print(len(cofeeShopArr))

# url='https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'
# page=requests.get(url)

# soup=BeautifulSoup(page.text, 'html.parser', )

# table = soup.find_all('table', class_='wikitable')[0]

# column_names = table.find_all('th', scope='col')

# column_titles = [title.text.strip() for title in column_names]


# print(column_titles)