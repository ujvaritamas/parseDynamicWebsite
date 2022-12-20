from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

url = "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0"

browser = webdriver.Firefox()
browser.get(url)
delay = 20 # seconds
try:
    #myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="leaderboardSponsorVisible"]/div/div[3]/div[1]')))
    myElems = WebDriverWait(browser, delay).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="leaderboardSponsorVisible"]/div/div[3]/div[1]')))
    myElems = WebDriverWait(browser, delay).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="leaderboardSponsorVisible"]/div/div[2]')))
    myElems = WebDriverWait(browser, delay).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'mobile athletes')))
    
    print("Page is ready!")
    #all_children_by_xpath = myElem.parent.find_elements(By.XPATH,".//*")
    print(myElems)
    print(myElems[0].get_attribute("class"))
    #all_children_by_xpath = myElem.parent.find_elements(By.XPATH,'.//*[@id="leaderboardSponsorVisible"]/div/div[3]/div')

    #for child in all_children_by_xpath:
    #    print(child)
        #if child.get_attribute('class') == 'athlete collapsed':
        #    print(child)
except TimeoutException:
    myElems = WebDriverWait(browser, delay).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="leaderboardSponsorVisible"]/div/div[3]/div[1]')))
    print(myElems[0].get_attribute("class"))
    print("Loading took too much time!")
finally:
    browser.quit()



#print(myElem)
#print(myElem.parent)