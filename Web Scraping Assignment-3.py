#!/usr/bin/env python
# coding: utf-8

# 1. Write a python program which searches all the product under a particular product from www.amazon.in. The 
# product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for 
# guitars.  

# In[ ]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time
import re

driver = webdriver.Chrome()
driver.get('https://www.amazon.in/')

inputU = input('please enter product here--->')

search_bar = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')   
search_bar.send_keys(inputU)       
search_button = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')   
search_button.click()        

productName=[]
PName=driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
for i in PName:
    if i.text is None :
        productName.append("--") 
    else:
        productName.append(i.text)
print(len(productName),productName)


# 2. In the above question, now scrape the following details of each product listed in first 3 pages of your search 
# results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then 
# scrape all the products available under that product name. Details to be scraped are: "Brand  
# Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and  
# “Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“.  

# In[ ]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time
import re

driver = webdriver.Chrome()
driver.get('https://www.amazon.in/')

start_page = 0
end_page = 3
urls = []
for page in range(start_page,end_page+1):
    try:
        page_urls = driver.find_elements_by_xpath('//a[@class="a-link-normal s-no-outline"]')
        
        # appending all the urls on current page to urls list
        for url in page_urls:
            url = url.get_attribute('href')     # Scraping the url from webelement
            if url[0:4]=='http':                # Checking if the scraped data is a valid url or not
                urls.append(url)                # Appending the url to urls list
        print("Product urls of page {} has been scraped.".format(page+1))
        
        # Moving to next page
        nxt_button = driver.find_element_by_xpath('//li[@class="a-last"]/a')      # Locating the next_button which is active
        if nxt_button.text == 'Next→':                                            # Checking if the button located is next button
            nxt_button.click()                                                    # Clicking the next button
            time.sleep(5)                                                         # time delay of 5 seconds
        # If the current active button is not next button, the we will check if the next button is inactive or not    
        elif driver.find_element_by_xpath('//li[@class="a-disabled a-last"]/a').text == 'Next→':    
            print("No new pages exist. Breaking the loop")  # Printing message and breakinf loop if we have reached the last page
            break
            
    except StaleElementReferenceException as e:             # Handling StaleElement Exception   
        print("Stale Exception")
        next_page = nxt_button.get_attribute('href')        # Extracting the url of next page
        driver.get(next_page)  

prod_dict = {}
prod_dict['Brand']=[]
prod_dict['Name']=[]
prod_dict['Rating']=[]
prod_dict['No. of ratings']=[]
prod_dict['Price']=[]
prod_dict['Return/Exchange']=[]
prod_dict['Expected Delivery']=[] 
prod_dict['Availability']=[]
prod_dict['Other Details']=[]
prod_dict['URL']=[]

for url in urls[:4]:
    driver.get(url)                                                        # Loading the webpage by url
    print("Scraping URL = ", url)
    #time.sleep(2)
    
    try:
        brand = driver.find_element_by_xpath('//a[@id="bylineInfo"]')      # Extracting Brand from xpath
        prod_dict['Brand'].append(brand.text)
    except NoSuchElementException:
        prod_dict['Brand'].append('-')
    
    try:
        name = driver.find_element_by_xpath('//h1[@id="title"]/span')      # Extracting Name from xpath
        prod_dict['Name'].append(name.text)
    except NoSuchElementException:
        prod_dict['Name'].append('-')
    
    try:
        rating = driver.find_element_by_xpath('//span[@id="acrPopover"]')  # Extracting Ratings from xpath
        prod_dict['Rating'].append(rating.get_attribute("title"))
    except NoSuchElementException:
        prod_dict['Rating'].append('-')
    
    try:
        n_rating = driver.find_element_by_xpath('//a[@id="acrCustomerReviewLink"]/span')     # Extracting no. of Ratings from xpath
        prod_dict['No. of ratings'].append(n_rating.text)
    except NoSuchElementException:
        prod_dict['No. of ratings'].append('-')
    
    try:
        price = driver.find_element_by_xpath('//span[@id="priceblock_ourprice"]')            # Extracting Price from xpath
        prod_dict['Price'].append(price.text)
    except NoSuchElementException:
        prod_dict['Price'].append('-')
    try:                                                                                     # Extracting Return/Exchange policy from xpath
        ret = driver.find_element_by_xpath('//div[@data-name="RETURNS_POLICY"]/span/div[2]/a')
        prod_dict['Return/Exchange'].append(ret.text)
    except NoSuchElementException:
        prod_dict['Return/Exchange'].append('-')
    try:
        delivry = driver.find_element_by_xpath('//div[@id="ddmDeliveryMessage"]/b')         # Extracting Expected Delivery from xpath
        prod_dict['Expected Delivery'].append(delivry.text)
    except NoSuchElementException:
        prod_dict['Expected Delivery'].append('-')
    
    try:
        avl = driver.find_element_by_xpath('//div[@id="availability"]/span')                # Extracting Availability from xpath
        prod_dict['Availability'].append(avl.text)
    except NoSuchElementException:
        prod_dict['Availability'].append('-')
    
    try:                                                                                    # Extracting Other Details from xpath
        dtls = driver.find_element_by_xpath('//ul[@class="a-unordered-list a-vertical a-spacing-mini"]')
        prod_dict['Other Details'].append('  ||  '.join(dtls.text.split('\n')))
    except NoSuchElementException:
        prod_dict['Other Details'].append('-')
    
    prod_dict['URL'].append(url)                                                            # Saving url
    time.sleep(2)
    
prod_df = pd.DataFrame.from_dict(prod_dict)
prod_df

prod_df.to_csv('Amazon_{}.csv'.format(inputU))


# 3. Write a python program to access the search bar and search button on images.google.com and scrape 10 
# images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’.

# In[ ]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time
import re

driver = webdriver.Chrome()
driver.get('https://images.google.com/')

search_bar = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')    
search_bar.send_keys("fruits")       
search_button = driver.find_element_by_xpath('//*[@id="sbtc"]/button')   
search_button.click() 

print("start scrolling to generate more images on the page...")
for _ in range(500):
    driver.execute_script("window.scrollBy(0,10000)")
    
images = driver.find_elements_by_xpath('//img[@class="rg_i Q4LuWd"]')

img_urls = []
img_data = []
for image in images:
    source= image.get_attribute('src')
    if source is not None:
        if(source[0:4] == 'http'):
            img_urls.append(source)
len(img_urls)

for i in range(len(img_urls)):
    if i >= 100:
        break
    print("Downloading {0} of {1} images" .format(i, 100))
    response= requests.get(img_urls[i])
    file = open("H:/Flip ROBO/banana/img"+str(i)+".jpg", "wb")
    file.write(response.content)
    


# 4. Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com 
# and scrape following details for all the search results displayed on 1st page. Details to be scraped: “Brand 
# Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”,  
# “Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the 
# details is missing then replace it by “- “. Save your results in a dataframe and CSV.  

# In[2]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time
import re

driver = webdriver.Chrome()
url4="https://www.flipkart.com/search?q=smartphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
driver.get(url4)

Brand_Name=[]
Colour=[]
Storage_RAM_ROM=[]
P_F_Camera=[]
Display_size_Resolution=[]
ProcessorAndCores=[]
Battery=[]
Price=[]
Product_URL=[]

BName=driver.find_elements_by_xpath("//div[@class='_4rR01T']")
for i in BName:
    if i.text is None :
        Brand_Name.append("--") 
    else:
        Brand_Name.append(i.text)
print(len(Brand_Name),Brand_Name)

ram=driver.find_elements_by_xpath("//ul[@class='_1xgFaf']//li[1]")
for i in ram:
    if i.text is None :
        Storage_RAM_ROM.append("--") 
    else:
        Storage_RAM_ROM.append(i.text)
print(len(Storage_RAM_ROM),Storage_RAM_ROM)

PC=driver.find_elements_by_xpath("//ul[@class='_1xgFaf']//li[3]")
for i in PC:
    if i.text is None :
        P_F_Camera.append("--") 
    else:
        P_F_Camera.append(i.text)
print(len(P_F_Camera),P_F_Camera)

DS=driver.find_elements_by_xpath("//ul[@class='_1xgFaf']//li[2]")
for i in DS:
    if i.text is None :
        Display_size_Resolution.append("--") 
    else:
        Display_size_Resolution.append(i.text)
print(len(Display_size_Resolution),Display_size_Resolution)

P=driver.find_elements_by_xpath("//ul[@class='_1xgFaf']//li[5]")
for i in P:
    if i.text is None :
        ProcessorAndCores.append("--") 
    else:
        ProcessorAndCores.append(i.text)
print(len(ProcessorAndCores),ProcessorAndCores)

B=driver.find_elements_by_xpath("//ul[@class='_1xgFaf']//li[4]")
for i in B:
    if i.text is None :
        Battery.append("--") 
    else:
        Battery.append(i.text)
print(len(Battery),Battery)

price=driver.find_elements_by_xpath("//div[@class='_30jeq3 _1_WHN1']")
for i in price:
    if i.text is None :
        Price.append("--") 
    else:
        Price.append(i.text)
print(len(Price),Price)

FlipKart=pd.DataFrame([])
FlipKart['Brand_Name']=Brand_Name
FlipKart['Storage_RAM_ROM']=Storage_RAM_ROM
FlipKart['Amount P_F_Camera']=P_F_Camera
FlipKart['Display_size_Resolution']=Display_size_Resolution
FlipKart['ProcessorAndCores']=ProcessorAndCores
FlipKart['Battery']=Battery
FlipKart['Price']=Price

FlipKart


# 5. Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps.

# In[1]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time
import re

driver = webdriver.Chrome()
driver.get("https://www.google.co.in/maps")
time.sleep(3)

city = input('Enter City Name : ')                                         # Enter city to be searched
search = driver.find_element_by_id("searchboxinput")                       # locating search bar
search.clear()                                                             # clearing search bar
time.sleep(2)
search.send_keys(city)                                                     # entering values in search bar
button = driver.find_element_by_id("searchbox-searchbutton")               # locating search button
button.click()                                                             # clicking search button
time.sleep(3)

try:
    url_string = driver.current_url
    print("URL Extracted: ", url_string)
    lat_lng = re.findall(r'@(.*)data',url_string)
    if len(lat_lng):
        lat_lng_list = lat_lng[0].split(",")
        if len(lat_lng_list)>=2:
            lat = lat_lng_list[0]
            lng = lat_lng_list[1]
        print("Latitude = {}, Longitude = {}".format(lat, lng))

except Exception as e:
        print("Error: ", str(e))


# 6. Write a program to scrap all the available details of best gaming laptops from digit.in. 

# In[ ]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time
import re

driver = webdriver.Chrome()
url1="https://trak.in/india-startup-funding-investment-2024/"
driver.get(url1)

Dates=[]
Company=[]
Industry=[]
Investor_Name=[]
Investment_Type=[]
Amount=[]

companies=driver.find_elements_by_xpath("//td[@class='column-3']")
for i in companies:
    if i.text is None :
        Company.append("--") 
    else:
        Company.append(i.text)
print(len(Company),Company)

Ind=driver.find_elements_by_xpath("//td[@class='column-4']")
for i in Ind:
    if i.text is None :
        Industry.append("--") 
    else:
        Industry.append(i.text)
print(len(Industry),Industry)

dt=driver.find_elements_by_xpath("//td[@class='column-2']")
for i in dt:
    if i.text is None :
        Dates.append("--") 
    else:
        Dates.append(i.text)
print(len(Dates),Dates)

IN=driver.find_elements_by_xpath("//td[@class='column-7']")
for i in IN:
    if i.text is None :
        Investor_Name.append("--") 
    else:
        Investor_Name.append(i.text)
print(len(Investor_Name),Investor_Name)

IT=driver.find_elements_by_xpath("//td[@class='column-8']")
for i in IT:
    if i.text is None :
        Investment_Type.append("--") 
    else:
        Investment_Type.append(i.text)
print(len(Investment_Type),Investment_Type)

Price=driver.find_elements_by_xpath("//td[@class='column-9']")
for i in Price:
    if i.text is None :
        Amount.append("--") 
    else:
        Amount.append(i.text)
print(len(Amount),Amount)

Funding=pd.DataFrame([])
Funding['Company']=Company
Funding['Industry']=Industry
Funding['Investor_Name']=Investor_Name
Funding['Amount Invested']=Amount
Funding['Specification']=Investment_Type
Funding['Dates']=Dates
Funding


# 7. Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped: 
# “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”.  

# In[ ]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time
import re

driver = webdriver.Chrome()
url="https://www.digit.in/top-products/best-gaming-laptops-40.html"

driver.get(url)

Brands=[]
Products_Description=[]
Specification=[]
Price=[]

br=driver.find_elements_by_xpath("//div[@class='TopNumbeHeading active sticky-footer']")
len(br)

for i in br:
   
    Brands.append(str(i.text).replace("\n",""))
Brands

sp=driver.find_elements_by_xpath("//div[@class='Specs-Wrap']")
len(sp)

for i in sp:
   
    Specification.append(str(i.text).replace("\n",""))
Specification

des=driver.find_elements_by_xpath("//div[@class='Section-center']")
len(des)

for i in des:
   
    Products_Description.append(str(i.text).replace("\n",""))
Products_Description

pri=driver.find_elements_by_xpath("//td[@class='smprice']")
len(pri)

for i in pri:
   
    Price.append(str(i.text).replace("\n",""))
Price

digit_lap=pd.DataFrame([])
digit_lap['Brands']=Brands[0:10]
digit_lap['Price']=Price[0:10]
digit_lap['Specification']=Specification[0:10]
digit_lap['Description']=Products_Description[0:10]
digit_lap


# 8. Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted 
# from any YouTube Video.  

# In[ ]:


from selenium import webdriver
import time

driver = webdriver.Chrome()  
video_url = 'https://www.youtube.com/watch?v=your_video_id'  
driver.get(video_url)

scroll_pause_time = 2  
scrolls = 10  

for _ in range(scrolls):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(scroll_pause_time)

comments = driver.find_elements_by_xpath('//yt-formatted-string[@id="content-text"]')
upvotes = driver.find_elements_by_xpath('//span[@id="vote-count-middle"]')
times = driver.find_elements_by_xpath('//a[@class="yt-simple-endpoint style-scope yt-formatted-string"]')

extracted_data = []
for comment, upvote, time in zip(comments, upvotes, times):
    extracted_data.append({'comment': comment.text, 'upvote': upvote.text, 'time': time.text })

driver.quit()

for data in extracted_data:
    print(data)


# 9. Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in 
# “London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall 
# reviews, privates from price, dorms from price, facilities and property description.  

# In[ ]:


import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = "https://www.hostelworld.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

hostels = soup.find_all("div", class_="fabresult")

for hostel in hostels:
    name = hostel.find("h2", class_="fabresult-title").text.strip()
  
    distance = hostel.find("span", class_="distance").text.strip()
  
    ratings = hostel.find("div", class_="rating").text.strip()
  
    total_reviews = hostel.find("div", class_="reviews").text.strip()
  
    overall_reviews = hostel.find("div", class_="overall").text.strip()
  
    privates_price = hostel.find("div", class_="price-col").find("div", class_="price").text.strip()
  
    dorms_price = hostel.find("div", class_="price-col").find("div", class_="price").find_next_sibling("div", class_="price").text.strip()
  
    facilities = hostel.find("div", class_="facilities").text.strip()
  
    description = hostel.find("div", class_="description").text.strip()
  
    print("Hostel Name:", name)
    print("Distance from City Centre:", distance)
    print("Ratings:", ratings)
    print("Total Reviews:", total_reviews)
    print("Overall Reviews:", overall_reviews)
    print("Privates from Price:", privates_price)
    print("Dorms from Price:", dorms_price)
    print("Facilities:", facilities)
    print("Property Description:", description)
    print()

