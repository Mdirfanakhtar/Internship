#!/usr/bin/env python
# coding: utf-8

# In[1]:


#All Requrired Library

# import debugger
import re

# selenium
import selenium
import pandas as pd
from selenium import webdriver

# Beautiful soup
from bs4 import BeautifulSoup
import requests

# add time
import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from selenium.webdriver.support.ui import WebDriverWait


# 1. Scrape  the details  of  most  viewed  videos  on YouTube from  Wikipedia.  
# Url = https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos You need to find following details:  A) 
# Rank   
# B) Name   
# C) Artist   
# D) Upload date   
# E) Views  

# In[2]:


# first, connect to the webdriver
driver=webdriver.Chrome()

# getting the webpage of mentioned url
url = 'https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos'
driver.get(url)
    


# In[3]:


# creating empty list for scraping the data

Rank = []
Name = []
Artist = []
Date = []
Views = []


# In[4]:


# scraping Rank of the videos
try:
    for i in driver.find_elements_by_xpath("//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[1]"):
        Rank.append(i.text)
except NoSuchElementException:
    Rank.append("-")
        
# Scraping Name of the videos
try:
    for i in driver.find_elements_by_xpath("//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[2]"):
        Name.append(i.text)
except NoSuchElementException:
    Name.append("-")
        
# Scraping Artist of the videos
try:
    for i in driver.find_elements_by_xpath("//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[3]"):
        Artist.append(i.text)
except NoSuchElementException:
    Artist.append("-")
        
# Scraping Upload_Date of the videos
try:
    for i in driver.find_elements_by_xpath("//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[5]"):
        Date.append(i.text)
except NoSuchElementException:
    Date.append("-")
        
# Scraping Views of the videos
try:
    for i in driver.find_elements_by_xpath("//table[@class='wikitable sortable jquery-tablesorter'][1]/tbody/tr/td[4]"):
        Views.append(i.text)
except NoSuchElementException:
    Views.append("-")
        
# creating DataFrame for scraped data
Wiki = pd.DataFrame({})
Wiki['Rank'] = Rank
Wiki['Name'] = Name
Wiki['Artist'] = Artist
Wiki['Upload Date'] = Date
Wiki['Views (in Billions)'] = Views

# removing stray numbers from Name column
Wiki.Name = Wiki.Name.apply(lambda x:x[:-4].strip('"'))
Wiki


# In[5]:


print(len(Rank),
len(Name),
len(Artist),
len(Date),
len(Views))


# In[6]:


driver.close()


# 2. Scrape the details team India’s international fixtures from bcci.tv.   
# Url = https://www.bcci.tv/.   
# You need to find following details:   
# A) Series   
# B) Place   
# C) Date   
# D) Time   
# Note: - From bcci.tv home page you have reach to the international fixture page through code.   

# In[2]:


# connecting to the webdriver
driver=webdriver.Chrome()

# getting the webpage of mentioned url
url=('https://www.bcci.tv/')
driver.get(url)


# In[3]:


btn=driver.find_element_by_xpath("//div[@class='navigation__drop-down drop-down drop-down--reveal-on-hover']/div/ul/li/a")
driver.get(btn.get_attribute("href"))
time.sleep(3)

# creating empty lists for scraping the data
Match_Title = []
Series = []
Place = []
Date = []
Time = []


# In[4]:


for i in driver.find_elements_by_xpath("//div[@class='fixture__format-strip']/span[@class='u-unskewed-text fixture__format']"):
    Match_Title.append(i.text)
    
for i in driver.find_elements_by_xpath("//div[@class='fixture__format-strip']/span[@class='u-unskewed-text fixture__tournament-label u-truncated']"):
    Series.append(i.text)
    
for i in driver.find_elements_by_xpath("//div[@class='fixture__description u-unskewed-text']/p/span"):
    Place.append(i.text)
        
for i in driver.find_elements_by_xpath("//span[@class='fixture__datetime tablet-only']/strong[1]"):
    Date.append(i.text.replace('\n',' '))

date=[i.split(' ',3)[:3] for i in Date]
date=[' '.join(i) for i in date]
Time=[i.split(' ',3)[-1] for i in Date]

# creating data frame
fixture=pd.DataFrame({'Match Title': Match_Title,
                          "Series": Series,
                          "Place": Place,
                          "Date": date,
                          "Time": Time})
fixture


# In[5]:


len(url)


# In[7]:


driver.close()


# 3. Scrape the details of State-wise GDP of India from statisticstime.com.   
# Url = http://statisticstimes.com/   
# You have to find following details: A) Rank   
# B) State   
# C) GSDP(18-19)- at current prices   
# D) GSDP(19-20)- at current prices   
# E) Share(18-19)   
# F) GDP($ billion)   
# Note: - From statisticstimes home page you have to reach to economy page through code. 

# In[6]:


# connecting to the web driver
driver=webdriver.Chrome()

# getting the webpage of mentioned url
url = ("https://statisticstimes.com/")
driver.get(url)


# In[8]:


# clicking on Economy button
driver.find_element_by_xpath("//div[@class='navbar']/div[2]/button").click()

# clicking on India
driver.find_element_by_xpath("//div[@class='dropdown-content']/a[3]").click()
time.sleep(3)

# clicking on GDP of Indian Economy
GDP = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/ul/li[1]/a").click()
time.sleep(3)


# In[9]:


# creating empty list
Rank = []
State = []
GSDP1 = []
GSDP2 = []
Share = []
GDP_billion = []

# scraping Rank
try:
    for i in driver.find_elements_by_xpath("//table[@class='display dataTable']/tbody/tr/td[1]"):
        Rank.append(i.text)
except NoSuchElementException:
    Rank.append("_")
    
# scraping State
try:
    for i in driver.find_elements_by_xpath("//table[@class='display dataTable']/tbody/tr/td[2]"):
        State.append(i.text)
except NoSuchElementException:
    State.append("_")
    
# scraping GSDP at current price (19-20)
try:
    for i in driver.find_elements_by_xpath("//table[@class='display dataTable']/tbody/tr/td[3]"):
        GSDP1.append(i.text)
except NoSuchElementException:
    GSDP1.append("_")
    
# scraping GSDP at current price (18-19)
try:
    for i in driver.find_elements_by_xpath("//table[@class='display dataTable']/tbody/tr/td[4]"):
        GSDP2.append(i.text)
except NoSuchElementException:
    GSDP2.append("_")
    
# scraping Share (18-19)
try:
    for i in driver.find_elements_by_xpath("//table[@class='display dataTable']/tbody/tr/td[5]"):
        Share.append(i.text)
except NoSuchElementException:
    Share.append("_")
    
# scraping GDP $ billion
try:
    for i in driver.find_elements_by_xpath("//table[@class='display dataTable']/tbody/tr/td[6]"):
        GDP_billion.append(i.text)
except NoSuchElementException:
    GDP_billion.append("_")
    
    
# creating DataFrame from the scraped data
GDP = pd.DataFrame({})
GDP['Rank'] = Rank
GDP['State'] = State
GDP['GSDP at current price (19-20)'] = GSDP1
GDP['GSDP at current price (18-19)'] = GSDP2
GDP['Share (18-19)'] = Share
GDP['GDP($ billion)'] = GDP_billion
GDP
    
    
        


# In[10]:


driver.close()


# 4. Scrape the details of trending repositories on Github.com.   
# Url = https://github.com/   
# You have to find the following details:   
# A) Repository title   
# B) Repository description   
# C) Contributors count   
# D) Language used  
# 
# Note: - From the home page you have to click on the trending option from Explore menu through code.

# In[2]:


# connecting to the web driver
driver=webdriver.Chrome()

# getting the webpage of mentioned url
url = ("https://github.com/")
driver.get(url)


# In[3]:


# getting explore button and clicking on it
explore = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/nav/ul/li[4]/details").click()

# selecting trending option
trend_url = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/nav/ul/li[4]/details/div/ul[2]/li[3]/a")
urls = trend_url.get_attribute("href")
driver.get(urls)


# In[4]:


# creating empty list
URLs = []
repository_title = []
Description = []
Contributors = []
Language = []
lang = []

# fetching urls for each repository
repository = driver.find_elements_by_xpath("//h1[@class='h3 lh-condensed']//a")
for i in repository:
    URLs.append(i.get_attribute("href"))
    
# scraping Repository title data
title = driver.find_elements_by_xpath("//h1[@class = 'h3 lh-condensed']")
for i in title:
    repository_title.append(i.text)
    
# scraping data from all repository page
for i in URLs:
    driver.get(i)
    time.sleep(5)
    
    # scraping Repository Description data 
    try:
        desc = driver.find_element_by_xpath("//p[@class='f4 mt-3']")
        Description.append(desc.text)
    except NoSuchElementException:
        Description.append('-')
        
        
    # scraping Contributors Count data
    try:
        contributor = driver.find_element_by_xpath("//*[contains(text(),'    Contributors ')]")
        Contributors.append(contributor.text.replace('Contributors',''))
    except NoSuchElementException:
        Contributors.append('-')
    
    
    # scraping Languages used data
    try:
        for i in driver.find_elements_by_xpath("//ul[@class= 'list-style-none']//li//span[1]"):
            lang.append(i.text)
        Language.append(lang)
    except NoSuchElementException:
        Language.append('-')
        
        
# Data Framing
Github = pd.DataFrame({})
Github['Repository Title'] = repository_title
Github['Repository Description'] = Description
Github['Contributors Count'] = Contributors
Github['Language Used'] = Language
Github


# In[5]:


driver.close()


# 5. Scrape the details of top 100 songs on billiboard.com. Url = https:/www.billboard.com/  You have to find the 
# following details:   
# A) Song name   
# B) Artist name   
# C) Last week rank   
# D) Peak rank   
# E) Weeks on board   
# Note: - From the home page you have to click on the charts option then hot 100-page link through code.  

# In[34]:


# connecting to the web driver
driver=webdriver.Chrome()

# getting the webpage of mentioned url
url = ("https://www.billboard.com/")
driver.get(url)


# In[36]:


# clicking on option button
charts=driver.find_element_by_xpath("//a[@class='header__main-link header__main-link--charts']").click()


# In[38]:


# creating empty lists
Song_Name = []
Artist_Name =[]
Last_week_rank = []
Peak_rank = []
Weeks_on_board = []

# getting urls for top 100 songs
urls = driver.find_element_by_xpath("//li[@class='header__submenu__list__element']//a")
page_url = urls.get_attribute("href")
driver.get(page_url)
time.sleep(4)

# scraping data of song names
for i in driver.find_elements_by_xpath("//span[@class='chart-element__information__song text--truncate color--primary']"):
    Song_Name.append(i.text)
    
# scraping data of artist names
for i in driver.find_elements_by_xpath("//span[@class='chart-element__information__artist text--truncate color--secondary']"):
    Artist_Name.append(i.text)
    
# scraping data of last week ranks
for i in driver.find_elements_by_xpath("//div[@class='chart-element__meta text--center color--secondary text--last']"):
    Last_week_rank.append(i.text)
    

# scraping data of peak ranks
for i in driver.find_elements_by_xpath("//div[@class='chart-element__meta text--center color--secondary text--peak']"):
    Peak_rank.append(i.text)       
    
    
# scraping data of weeks on board
for i in driver.find_elements_by_xpath("//div[@class='chart-element__meta text--center color--secondary text--week']"):
    Weeks_on_board.append(i.text)
    
    
# creating dataframe for scraped data
billiboard = pd.DataFrame({})
billiboard['Name'] = Song_Name
billiboard['Artist'] = Artist_Name
billiboard['Last Week Rank'] = Last_week_rank
billiboard['Peak Rank'] = Peak_rank
billiboard['Weeks on board'] = Weeks_on_board
billiboard


# In[39]:


driver.close()


# 6. Scrape the details of Highest selling novels.   
# A) Book name   
# B) Author name   
# C) Volumes sold   
# D) Publisher   
# E) Genre   
# Url - https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare 

# In[18]:


# connecting to the web driver
driver=webdriver.Chrome()

# getting the webpage of mentioned url
url = ("https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare/")
driver.get(url)
time.sleep(3)


# In[19]:


# creating empty lists
Book_name = []
Author_name = []
Volumes_sold = []
Publisher = []
Genre = []


# scraping book names data
for i in driver.find_elements_by_xpath("//tbody//tr//td[2]"):
    Book_name.append(i.text)

    
# scraping author names data
for i in driver.find_elements_by_xpath("//tbody//tr//td[3]"):
    try:
        if i.text == '0' : raise NoSuchElementException
        Author_name.append(i.text)
    except NoSuchElementException:
        Author_name.append('-')
time.sleep(3)


# scraping data of volumes sold
for i in driver.find_elements_by_xpath("//tbody//tr//td[4]"):
    Volumes_sold.append(i.text)
    
    
# scraping data of publisher names
for i in driver.find_elements_by_xpath("//tbody//tr//td[5]"):
    Publisher.append(i.text)
    
    
# scraping  data of genre
for i in driver.find_elements_by_xpath("//tbody//tr//td[6]"):
    Genre.append(i.text)    
    
    
# creating dataframe for scraped data
Novels = pd.DataFrame({})
Novels['Book Name'] = Book_name
Novels['Author'] = Author_name
Novels['Volume sold'] = Volumes_sold
Novels['Publisher'] = Publisher
Novels['Genre'] = Genre
Novels 


# In[20]:


driver.close()


# 7. Scrape the details most watched tv series of all time from imdb.com.   
# Url = https://www.imdb.com/list/ls095964455/ You have 
# to find the following details:   
# A) Name   
# B) Year span   
# C) Genre   
# D) Run time   
# E) Ratings   
# F) Votes   

# In[21]:


# connecting to the web driver
driver=webdriver.Chrome()

# getting the webpage of mentioned url
url = ("https://www.imdb.com/list/ls095964455/")
driver.get(url)


# In[22]:


# creating empty lists
Name = []
Year_span = []
Genre = []
Run_time = []
Ratings = []
Votes = []

# scraped data of Names
for i in driver.find_elements_by_xpath("//h3[@class='lister-item-header']/a"):
    Name.append(i.text)
    
    
# scraped data of Year span
for i in driver.find_elements_by_xpath("//span[@class='lister-item-year text-muted unbold']"):
    Year_span.append(i.text)
    
    
# scraped data of Genre
for i in driver.find_elements_by_xpath("//span[@class='genre']"):
    Genre.append(i.text)
    
    
# scraped data of Run time
for i in driver.find_elements_by_xpath("//span[@class='runtime']"):
    Run_time.append(i.text)
    
    
# scraped data of Ratings
for i in driver.find_elements_by_xpath("//div[@class='ipl-rating-star small']//span[2]"):
    Ratings.append(i.text)
    
    
# scraped data of Votes
for i in driver.find_elements_by_xpath("//div[@class='lister-item-content']//p[4]/span[2]"):
    Votes.append(i.text) 
    
    
# creating dataframe for scraped data
TV_Series = pd.DataFrame({})
TV_Series['Name'] = Name
TV_Series['Year Span'] = Year_span
TV_Series['Genre'] = Genre
TV_Series['Run Time'] = Run_time
TV_Series['Ratings'] = Ratings
TV_Series['Votes'] = Votes
TV_Series


# In[23]:


driver.close()


# 8. Details of Datasets from UCI machine learning repositories.   
# Url = https://archive.ics.uci.edu/  You 
# have to find the following details:   
# A) Dataset name   
# B) Data type   
# C) Task   
# D) Attribute type   
# E) No of instances   
# F) No of attribute G) Year   
# Note: - from the home page you have to go to the Show All Dataset page through code.   
# 

# In[7]:


# connecting to the web driver
driver=webdriver.Chrome()

# getting the webpage of mentioned url
url = (" https://archive.ics.uci.edu/")
driver.get(url)


# In[8]:


# fetching view all dataset button from the webpage
viewall_dataset = driver.find_element_by_xpath("//tbody[1]//tr/td[2]/span[2]/a")
page_url = viewall_dataset.get_attribute("href")
driver.get(page_url)
time.sleep(3)


# In[9]:


# fetching page urls of all datasets
view_list = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/p/a")
list_url = view_list.get_attribute("href")
driver.get(list_url)
time.sleep(3)


# In[10]:


# fetching urls for each dataset
dataset_url = driver.find_elements_by_xpath("//p[@class='normal']//b/a")

urls = []
for i in dataset_url:
    urls.append(i.get_attribute("href"))


# In[ ]:


# creating empty lists
Dataset_name = []
Data_type = []
Task = []
Attribute_type = []
No_of_instances = []
No_of_attributes = []
Year = []

for i in urls:
    driver.get(i)
    time.sleep(3)
    
    
    # scraping  Dataset name
    try:
        dataset_name = driver.find_element_by_xpath("//span[@class='heading']")
        Dataset_name.append(dataset_name.text)
    except NoSuchElementException:
        Dataset_name.append('-')
    time.sleep(3)
    
    
    
    # scraping data type
    try:
        data_type = driver.find_element_by_xpath("//table[@border='1']//tbody/tr/td[2]")
        if data_type.text == "N/A": raise NoSuchElementException
        Data_type.append(data_type.text)
    except NoSuchElementException:
        Data_type.append('-')
    time.sleep(3)
    
    
    # scraping Task
    try:
        task = driver.find_element_by_xpath("//table[@border='1']//tbody/tr[3]/td[2]")
        if task.text == "N/A": raise NoSuchElementException
        Task.append(task.text)
    except NoSuchElementException:
        Task.append('-')
    time.sleep(3)
    
    
    
    # scraping Attribute type
    try:
        attribute_type = driver.find_element_by_xpath("//table[@border='1']//tbody/tr[2]/td[2]")
        if attribute_type.text == "N/A": raise NoSuchElementException
        Attribute_type.append(attribute_type.text)
    except NoSuchElementException:
        Attribute_type.append('-')
    time.sleep(3)
    
    
    
    # scraping No of Instances
    try:
        instances = driver.find_element_by_xpath("//table[@border='1']//tbody/tr/td[4]")
        if instances.text == "N/A": raise NoSuchElementException
        No_of_instances.append(instances.text)
    except NoSuchElementException:
        No_of_instances.append('-')
    time.sleep(3)
    
    
    
    # scraping No of Arrtibutes
    try:
        attribute = driver.find_element_by_xpath("//table[@border='1']//tbody/tr[2]/td[4]")
        if attribute.text == "N/A": raise NoSuchElementException
        No_of_attributes.append(attribute.text)
    except NoSuchElementException:
        No_of_attributes.append('-')
    time.sleep(3)
    
    
    # scraping Year
    try:
        year = driver.find_element_by_xpath("//table[@border='1']//tbody/tr[2]/td[6]")
        if year.text == "N/A": raise NoSuchElementException
        Year.append(year.text[:4])
    except NoSuchElementException:
        Year.append('-')
    time.sleep(3)
    


# In[ ]:


# creating dataframe for scraped data
ML = pd.DataFrame({})
ML['Data Name'] = Data_name 
ML['Data Type '] = Data_type
ML['Task '] = Task 
ML['Attribute Type '] = Attribute_type 
ML['No of Instance '] = No_of_instances
ML['No of Attributes '] = No_of_attributes 
ML['Year '] = Year 
ML


# In[ ]:


driver.close()

