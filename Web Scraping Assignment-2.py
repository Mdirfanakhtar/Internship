#!/usr/bin/env python
# coding: utf-8

# Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You
# have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10
# jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Analyst” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the searchbutton.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manually.

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Set up the Chrome webdriver
chrome_driver_path = "path_to_chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Open Shine.com and search for Data Analyst jobs in Bangalore
driver.get("https://www.shine.com/")
job_title = driver.find_element(By.ID, "qsb-keyskill-sugg")
job_title.send_keys("Data Analyst")
location = driver.find_element(By.ID, "qsb-location-sugg")
location.send_keys("Bangalore")
search_button = driver.find_element(By.CLASS_NAME, "btn")
search_button.click()

# Scrape the data for the first 10 jobs
job_titles = driver.find_elements(By.CLASS_NAME, "job_title")
job_locations = driver.find_elements(By.CLASS_NAME, "loc")
company_names = driver.find_elements(By.CLASS_NAME, "company")
experience_required = driver.find_elements(By.CLASS_NAME, "exp")

# Store the scraped data in lists
titles = [title.text for title in job_titles[:10]]
locations = [location.text for location in job_locations[:10]]
companies = [company.text for company in company_names[:10]]
experience = [exp.text for exp in experience_required[:10]]

# Create a DataFrame
data = {
    "Job Title": titles,
    "Job Location": locations,
    "Company Name": companies,
    "Experience Required": experience
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Close the webdriver
driver.quit()


# Q2:Write a python program to scrape data for “Data Scientist” Job position in“Bangalore” location. You
# have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Scientist” in “Job title, Skills” field and enter “Bangalore” in “enter thelocation” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manually.
# 

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to Shine.com
driver.get("https://www.shine.com/")

# Find and fill the job title field
job_title_field = driver.find_element(By.ID, "qsb-keyword-sugg")
job_title_field.send_keys("Data Scientist")

# Find and fill the location field
location_field = driver.find_element(By.ID, "qsb-location-sugg")
location_field.send_keys("Bangalore")

# Click the search button
search_button = driver.find_element(By.CLASS_NAME, "qsb-search-btn")
search_button.click()

# Wait for the page to load
driver.implicitly_wait(5)

# Scrape the data for the first 10 job results
jobs = driver.find_elements(By.XPATH, "//li[@class='sri']/a")
job_titles = []
job_locations = []
company_names = []

for job in jobs[:10]:
    job.click()
    driver.switch_to.window(driver.window_handles[1])
    job_title = driver.find_element(By.CLASS_NAME, "job_title")
    job_titles.append(job_title.text.strip())
    job_location = driver.find_element(By.CLASS_NAME, "loc")
    job_locations.append(job_location.text.strip())
    company_name = driver.find_element(By.CLASS_NAME, "job_cmp_name")
    company_names.append(company_name.text.strip())
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# Create a dataframe
data = {
    'Job Title': job_titles,
    'Job Location': job_locations,
    'Company Name': company_names
}

df = pd.DataFrame(data)

# Print the dataframe
print(df)

# Close the WebDriver
driver.quit()


# Q3: In this question you have to scrape data using the filters available on the webpage 
#  You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required.
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps:
# 1. first get the web page https://www.shine.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
# 3. Then click the search button.
# 4. Then apply the location filter and salary filter by checking the respective boxes
# 5. Then scrape the data for the first 10 jobs results you get.
# 6. Finally create a dataframe of the scrapeddata.
# Note: All of the above steps have to be done in code. No step is to be done manually.

# In[ ]:


import selenium
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome()

url = "https://www.shine.com"
driver.get(url)

search_job = driver.find_element_by_xpath("//input[@class='sugInp']")
search_job

search_job.send_keys('Data Scientist')
search_btn= driver .find_element_by_xpath("//button[@class='btn']")
search_btn

search_btn=driver.find_element_by_class_name('btn')
search_btn.click()

title_t1=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
title_t1

job_titles=[]
for i in title_t1:
    if i.text is None:
        job_titles.append('Not')
    else:
        job_titles.append(i.text)
        
job_titles[:10]   
company_t1=driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
company_t1

companies_names=[]

for i in company_t1:
    companies_names.append(i.text)
    
companies_names[:10]    
experience_t1=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience'] //span")
experience_t1

experience_list=[]

for i in experience_t1:
    experience_list.append(i.text)
    
experience_list[:10]   
locations_t1=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']/span")
locations_t1

locations_list=[]

for i in locations_t1:
    locations_list.append(i.text)
    
locations_list[:10]  
print(len(job_titles[:10])),print(len(companies_names[:10])),print(len(experience_list[:10])),print(len(locations_list[:10]))



jobs2=pd.DataFrame({})
jobs2['title']=job_titles[:10]
jobs2['company']=companies_names[:10]
jobs2['experience_required']=experience_list[:10]
jobs2['location']=locations_list[:10]

jobs2


# Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 6. Brand
# 7. ProductDescription
# 8. Price
# The attributes which you have to scrape is ticked marked in the below image.
# To scrape the data you have to go through following steps:
# 1. Go to Flipkart webpage by url :https://www.flipkart.com/
# 2. Enter “sunglasses” in the search fieldwhere “search for products, brands and more” is written and
# click the search icon
# 3. After that you will reach to the page having a lot of sunglasses. From this page you can scrap the
# required data as usual.
# 4. After scraping data from the first page, go to the “Next” Button at the bottom other page , then
# click on it.
# 5. Now scrape data from this page as usual
# 6. Repeat this until you get data for 100sunglasses.
# Note: That all of the above steps have to be done by coding only and not manually.

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.flipkart.com/')

search_box = driver.find_element(By.XPATH, "//input[@title='Search for products, brands and more']")
search_box.send_keys('sunglasses')
search_box.submit()

sunglasses = driver.find_elements(By.XPATH, "//div[@class='_2kHMtA']")
data = []

for i in range(100):
    brand = sunglasses[i].find_element(By.XPATH, ".//div[@class='_2WkVRV']")
    description = sunglasses[i].find_element(By.XPATH, ".//a[@class='IRpwTa']")
    price = sunglasses[i].find_element(By.XPATH, ".//div[@class='_30jeq3 _1_WHN1']")
  
    data.append({'Brand': brand.text, 'ProductDescription': description.text, 'Price': price.text})
    
for item in data:
    print(item)


# Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:
# https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market
# place=FLIPKART
# 
# As shown in the above page you have to scrape the tick marked attributes. These are:
# 1. Rating
# 2. Review summary
# 3. Full review
# 4. You have to scrape this data for first 100reviews.
# Note: All the steps required during scraping should be done through code only and not manually.
# 

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the Flipkart page for iPhone 11 reviews
url = "https://www.flipkart.com/apple-iphone-11-black-64-gb/product?reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART"
driver.get(url)

# Wait for the reviews section to load
reviews_section = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "col._390CkK._1gY8H-"))
)

# Initialize lists to store scraped data
ratings = []
review_summaries = []
full_reviews = []

# Scrape data for the first 100 reviews
while len(ratings) < 100:
    # Find all review blocks
    review_blocks = driver.find_elements_by_xpath("//div[@class='_27M-vq']")

    # Iterate through each review block
    for block in review_blocks:
        # Extract rating
        rating = block.find_element_by_xpath(".//div[@class='_3LWZlK _1BLPMq']").text
        ratings.append(rating)

        # Extract review summary
        summary = block.find_element_by_xpath(".//p[@class='_2-N8zT']").text
        review_summaries.append(summary)

        # Extract full review
        try:
            full_review = block.find_element_by_xpath(".//div[@class='t-ZTKy']/div/div").text
        except:
            full_review = "No full review available"
        full_reviews.append(full_review)

        # Check if we have scraped 100 reviews
        if len(ratings) == 100:
            break

    # If we haven't scraped 100 reviews yet, click on the next page button
    if len(ratings) < 100:
        try:
            next_button = driver.find_element_by_xpath("//a[@class='_1LKTO3']")
            next_button.click()
            WebDriverWait(driver, 10).until(EC.staleness_of(review_blocks[0]))
        except:
            break

# Print the scraped data
for i in range(100):
    print("Review", i+1)
    print("Rating:", ratings[i])
    print("Review Summary:", review_summaries[i])
    print("Full Review:", full_reviews[i])
    print("\n")

# Close the browser
driver.quit()


# Q6: Scrape data forfirst 100 sneakers you find whenyou visit flipkart.com and search for “sneakers” inthe
# search field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. ProductDescription
# 3. Price
# As shown in the below image, you have to scrape the above attributes.

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize Selenium WebDriver (make sure you have the appropriate driver installed, like ChromeDriver)
driver = webdriver.Chrome()

# Open Flipkart website
driver.get("https://www.flipkart.com/")

# Find the search bar and enter "sneakers"
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("sneakers")
search_bar.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(5)

# Scrape data for the first 100 sneakers
sneakers_data = []
while len(sneakers_data) < 100:
    # Find all the products on the page
    products = driver.find_elements(By.XPATH, "//div[@class='_2B099V']/a[@class='IRpwTa']")
    for product in products:
        # Extracting brand, description, and price
        brand = product.find_element(By.XPATH, ".//div[@class='_2WkVRV']").text
        description = product.find_element(By.XPATH, ".//a[@class='IRpwTa']").get_attribute("title")
        price = product.find_element(By.XPATH, ".//div[@class='_30jeq3']").text

        # Append the data to the list
        sneakers_data.append({
            "Brand": brand,
            "ProductDescription": description,
            "Price": price
        })
        # Check if we have reached 100 sneakers
        if len(sneakers_data) >= 100:
            break

    # If we haven't collected 100 sneakers yet, move to the next page
    if len(sneakers_data) < 100:
        next_page = driver.find_element(By.XPATH, "//a[@class='_1LKTO3'][contains(text(),'Next')]")
        next_page.click()
        time.sleep(5)  # Wait for the next page to load

# Print the scraped data
for idx, sneaker in enumerate(sneakers_data, start=1):
    print(f"Sneaker {idx}:")
    print(f"Brand: {sneaker['Brand']}")
    print(f"Description: {sneaker['ProductDescription']}")
    print(f"Price: {sneaker['Price']}")
    print()

# Close the browser
driver.quit()


# Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then
# set CPU Type filter to “Intel Core i7” as shown in the below image:
#     After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your webdriver executable
driver_path = 'your_driver_path_here'

# Initialize Chrome webdriver
driver = webdriver.Chrome(driver_path)

# Open the Amazon India website
driver.get('https://www.amazon.in/')

# Find the search field and enter "Laptop"
search_field = driver.find_element_by_id('twotabsearchtextbox')
search_field.send_keys('Laptop')

# Click the search icon
search_icon = driver.find_element_by_id('nav-search-submit-button')
search_icon.click()

# Wait for the CPU Type filter to load and click on "Intel Core i7"
cpu_filter = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'CPU Type')]/../.."))
)
cpu_filter.click()

intel_i7_filter = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Intel Core i7')]"))
)
intel_i7_filter.click()

# Wait for the results to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 's-result-list')))

# Scrape data for the first 10 laptops
laptops = driver.find_elements_by_css_selector('.s-result-item')

for laptop in laptops[:10]:
    # Extract title
    title = laptop.find_element_by_css_selector('h2.a-size-mini > a').text
    
    # Extract ratings
    try:
        ratings = laptop.find_element_by_css_selector('.a-popover-trigger .a-icon-alt').get_attribute('textContent')
    except:
        ratings = 'Not Available'
    
    # Extract price
    try:
        price = laptop.find_element_by_css_selector('.a-price-whole').text
    except:
        price = 'Not Available'
    
    # Print scraped dat
    print("Title:", title)
    print("Ratings:", ratings)
    print("Price:", price)
    print()

# Close the webdriver
driver.quit()


# Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
# 1. First get the webpagehttps://www.azquotes.com/
# 2. Click on TopQuotes
# 

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up Chrome webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless browser
service = Service('path_to_chromedriver')  # Provide path to chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Load webpage
url = "https://www.azquotes.com/"
driver.get(url)

# Click on TopQuotes
try:
    top_quotes_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[text()='Top Quotes']"))
    )
    top_quotes_link.click()
except TimeoutException:
    print("Loading Top Quotes link timed out.")

# Scrape the quotes
try:
    quotes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "title"))
    )
    for quote in quotes[:1000]:  # Scraping top 1000 quotes
        print(quote.text)
except TimeoutException:
    print("Loading quotes timed out.")

# Close the webdriver
driver.quit()

