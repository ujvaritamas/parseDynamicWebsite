import requests 
 
url = "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0"

 
response = requests.get(url) 
 
html = response.text 
 
print(html)

with open('test0.txt', 'w') as file:
    file.write(html)