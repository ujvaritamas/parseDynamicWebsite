from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def save_html():
    url = "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0"

    driver = webdriver.Chrome(service=ChromeService( 
        ChromeDriverManager().install())) 
    
    driver.implicitly_wait(30)
    driver.get(url)
    driver.implicitly_wait(30)

    time.sleep(5)
    
    print(driver.page_source)

    html = driver.page_source

    with open('test1.html', 'w') as file:
        file.write(html)
    
    driver.quit()

#save_html()




from bs4 import BeautifulSoup

with open("test1.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

print(soup.head.title)

import pdb; pdb.set_trace()
leaderbouard = soup.find_all(class_='main-content loading')

print(soup.find_all(class_='athlete-placement-stat-name'))