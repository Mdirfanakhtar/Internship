#!/usr/bin/env python
# coding: utf-8

# 1) Write a python program to display all the header tags from wikipedia.org and make data frame.

# In[4]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')
df= pd.DataFrame({'header_tags':titles, "id":id})
df


# 2) Write s python program to display list of respected former presidents of India(i.e. Name , Term of office)
# from https://presidentofindia.nic.in/former-presidents.htm and make data frame.

# In[5]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://presidentofindia.nic.in/former-presidents.htm"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table")
names = []
terms = []
for row in soup.find_all("tr")[1:]:
    columns = row.find_all("td")
    names = columns[0].text.strip()
    term = columns[1].text.strip()
    names.append(name)
    terms.append(term)
data = {"Name": names, "Term of Office": terms}
df = pd.DataFrame(data)
print(df)


# 3) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame
# a) Top 10 ODI teams in men’s cricket along with the records for matches,

# In[6]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
team_data = []
table = soup.find("table", class_="table")
rows = soup.find_all("tr")
for row in rows[1:11]:
    cells = row.find_all("td")
    team = cells[1].text.strip()
    matches = cells[2].text.strip()
    points = cells[3].text.strip()
    rating = cells[4].text.strip()
    team_data.append([team, matches, points, rating])
df = pd.DataFrame(team_data, columns=["Team", "Matches", "Points", "Rating"])
print(df)


# b) Top 10 ODI Batsmen along with the records of their team andrating.

# In[7]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
batsman_data = []
table = soup.find("table", class_="table")
rows = soup.find_all("tr")
for row in rows[1:11]:
    cells = row.find_all("td")
    batsman = cells[1].text.strip()
    team = cells[2].text.strip()
    rating = cells[3].text.strip()
    batsman_data.append([batsman, team, rating])
df = pd.DataFrame(batsman_data, columns=["Batsman", "Team", "Rating"])
print(df)


# c) Top 10 ODI bowlers along with the records of their team andrating.

# In[9]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
bowler_data = []
table = soup.find("table", class_="table")
rows = soup.find_all("tr")
for row in rows[1:11]:
    cells = row.find_all("td")
    bowler = cells[1].text.strip()
    team = cells[2].text.strip()
    rating = cells[3].text.strip()
    bowler_data.append([bowler, team, rating])
df = pd.DataFrame(bowler_data, columns=["Bowler", "Team", "Rating"])
print(df)


# 4) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://www.icc-cricket.com/rankings/womens/team-rankings/odi'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class': 'table'})
teams = []
matches = []
points = []
ratings = []
for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    teams.append(columns[0].text)
    matches.append(columns[1].text)
    points.append(columns[2].text)
    ratings.append(columns[3].text)
odi_team_rankings = pd.DataFrame({'Team': teams, 'Matches': matches, 'Points': points, 'Ratings': ratings})


# b) Top 10 women’s ODI Batting players along with the records of their team and rating.

# In[12]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class': 'table'})
players = []
teams = []
ratings = []
for row in soup.find_all('tr')[1:]:
    columns = row.find_all('td')
    players.append(columns[0].text)
    teams.append(columns[1].text)
    ratings.append(columns[2].text)
odi_batting_rankings = pd.DataFrame({
    'Player': players,
    'Team': teams,
    'Ratings': ratings
})


# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[13]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class': 'table'})
players = []
teams = []
records = []
ratings = []
for row in soup.find_all('tr'):
    player = row.find('td', {'class': 'player-name'}).text
    players.append(player)
    team = row.find('td', {'class': 'team-name'}).text
    teams.append(team)
    record = row.find('td', {'class': 'total-matches'}).text
    records.append(record)
    rating = row.find('td', {'class': 'rating'}).text
    ratings.append(rating)
odi_allrounders = pd.DataFrame({'Player': players, 'Team': teams, 'Records': records,'Ratings': ratings})
top_10_allrounders = odi_allrounders.head(10)
print(top_10_allrounders)


# 5) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and
# make data frame
# i) Headline
# ii) Time
# iii) News Link

# In[14]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://www.cnbc.com/world/?region=world'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
articles = soup.find_all('div', class_='LatestNews-item')
news_details = []
for article in articles:
    headline = article.find('h3').text
    time = article.find('time')['datetime']
    news_link = article.find('a')['href']
    news_details.append([headline, time, news_link])
df = pd.DataFrame(news_details, columns=['Headline', 'Time', 'News Link'])
print(df)


# 6. Write a python program to scrape the details of most downloaded articles from AI in last 90
# days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# Scrape below mentioned details and make data frame
# i) Paper Title
# ii) Authors
# iii) Published Date
# iv) Paper URL
# 

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
articles_container = soup.find("div", class_="pod-listing")
titles = []
authors = []
dates = []
urls = []
for article in articles_container.find_all("li"):
    title = article.find("h3").text.strip()
    titles.append(title)
    author = article.find("span", class_="text-xs").text.strip()
    authors.append(author)
    date = article.find("span", class_="text-xs").find_next_sibling("span").text.strip()
    dates.append(date)
    url = article.find("a")["href"]
    urls.append(url)
data = {"Paper Title": titles, "Authors": authors, "Published Date": dates, "Paper URL": urls}
df = pd.DataFrame(data)
print(df)


# 7) Write a python program to scrape mentioned details from dineout.co.inand make data framei) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.dineout.co.in"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
restaurant_names = soup.find_all('h2', class_='restnt-name ellipsis')
cuisines = soup.find_all('span', class_='double-line-ellipsis')
locations = soup.find_all('span', class_='double-line-ellipsis')
ratings = soup.find_all('span', class_='rating-value')
image_urls = soup.find_all('img', class_='img-responsive')
restaurant_list = []
cuisine_list = []
location_list = []
rating_list = []
image_url_list = []
for name in restaurant_names:
    restaurant_list.append(name.text.strip())
for cuisine in cuisines:
    cuisine_list.append(cuisine.text.strip())
for location in locations:
    location_list.append(location.text.strip())
for rating in ratings:
    rating_list.append(rating.text.strip())
for image in image_urls:
    image_url_list.append(image['src'])
data = {'Restaurant Name': restaurant_list, 'Cuisine': cuisine_list, 'Location': location_list, 'Ratings': rating_list, 'Image URL': image_url_list}
df = pd.DataFrame(data)
print(df)

