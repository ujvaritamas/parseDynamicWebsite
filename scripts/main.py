from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0"

driver = webdriver.Firefox()

driver.maximize_window()
driver.get(url)
driver.implicitly_wait(5)

#time.sleep(5)

#athletes = driver.find_elements(By.CLASS_NAME, "inner mobile")
#print(athletes)

#container = driver.find_element(By.CLASS_NAME, "container-overlay")
#print(container)

leaderboard = driver.find_element(By.ID, "leaderboard")
#print("leaderboard: {}".format(leaderboard))

#mobile_athletes = leaderboard.find_element(By.XPATH, '//*[@id="leaderboardSponsorVisible"]/div/div[3]')
#print("mobile_athletes: {}".format(mobile_athletes))


#print("::::::::::::::::::::::::::::::::::::::::")

driver.implicitly_wait(10)
print("hello")
driver.execute_script("window.scrollBy(0,500)","")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

time.sleep(6)

mobile_athletes = driver.find_element(By.XPATH, '//*[@id="leaderboardSponsorVisible"]/div/div[3]')
print("mobile_athletes: {}".format(mobile_athletes.get_attribute('class')))


#athletes = driver.find_elements(By.XPATH, '//*[@id="leaderboardSponsorVisible"]/div/div[3]')

#all_children_by_xpath = mobile_athletes.find_elements(By.XPATH,".//*")

#print(all_children_by_xpath)

driver.quit()

#athletes_collapsed = driver.find_elements(By.XPATH, '//*[@id="leaderboardSponsorVisible"]/div/div[3]/div[2]')
#print(athletes_collapsed)

#athletes = driver.find_element_by_class_name("athlete collapsed")

#for athlete in athletes:
#    name = athlete.find_element_by_xpath('//*[@id="leaderboardSponsorVisible"]/div/div[3]/div[1]/h3/span/span[3]')
#    print(name)