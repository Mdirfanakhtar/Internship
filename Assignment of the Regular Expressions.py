#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to replace all occurrences of a space, comma, or dot with a colon.

# In[1]:


text = input("Enter your string: ")
def your_string(text):
    for symbol in [' ', ',', '.']:
        text = text.replace(symbol, ':')
    return text
print("new string:", your_string(text))


# 2. Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXXX, ;, etc.) from the columns except words.

# In[34]:


import pandas as pd
dictionary = {'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']}
df = pd.DataFrame(data=dictionary)
df['SUMMARY'] = df['SUMMARY'].str.replace(r'[^\w\s]|[0-9]|[A-Z]', '')
print(df)
import warnings
warnings.filterwarnings("ignore")


# 3. Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.

# In[3]:


import re
text=input("enter your text: ")
result= re.findall(r"\w{4}",text)
print("match string: ",result)


# 4. Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

# In[4]:


import re
text=input("enter your text: ")
result= re.findall(r"\w{3,5}",text)
print("match string: ",result)


# 5. Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.

# In[5]:


import re
text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
for string in text:
    print(re.sub(r" ?\([^)]+\)", "", string))


# 6. Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.

# In[6]:


import re
with open('file.txt', 'r') as file:
    text = file.read()
def remove(text):
    return re.sub(r"\(.*?\)", "", text)
print("after removing: ",remove(text))


# 7. Write a regular expression in Python to split a string into uppercase letters.

# In[7]:


import re
text=input("enter your text: ")
result=re.findall("[A-Z][^A-Z]*",text)
print(result)


# 8. Create a function in python to insert spaces between words starting with numbers.

# In[8]:


import re
def string():
    text = input("Enter your text: ")
    new_text = re.sub(r"\B(?=\d)", " ", text)
    print("new text: ", new_text)
string()


# 9. Create a function in python to insert spaces between words starting with capital letters or with numbers.

# In[9]:


import re
def string():
    text = input("Enter your text: ")
    new_text = re.sub(r"\B(?=[A-Z\d])", " ", text)
    print(new_text)
string()


# 10. Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.

# In[1]:


import pandas as pd

url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"
df = pd.read_csv(url)
df["first_five_letters"] = df["Country"].str[:6]
print(df)


# 11. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

# In[13]:


import re
text= input("Enter your text: ")
match= re.findall(r"[A-Z]+|[a-z]+|[0-9]+|[_]+",text)
print("match string: ", match)


# 12. Write a Python program where a string will start with a specific number.

# In[14]:


import re
text= input("Enter your text: ")
def number(string):
    string = re.compile(r"^5")
    if string.match(text):
        return True
    else:
        return False
print(number('text'))


# 13. Write a Python program to remove leading zeros from an IP address.

# In[15]:


import re
ip = input("enter IP address: ")
string = re.sub('\.[0]*', '.', ip)
print(string)


# 14. Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.

# In[16]:


import re
with open('sample_text.txt', 'r') as f:
    text = f.read()
result = re.compile(r'(?P<month>\w+)\s+(?P<day>\d+)(?:th)?\s+(?P<year>\d+)')
match = result.search(text)
print(match.group())


# 15. Write a Python program to search some literals strings in a string.

# In[17]:


import re
text = 'The quick brown fox jumps over the lazy dog.'
literals_string = [ 'fox', 'dog', 'horse' ]
for literals in literals_string:
    print('Search literals string is: ', (literals))
    if re.search(literals,  text):
        print((literals), 'is present in the string')
    else:
        print((literals), 'is Not present in the string')


# 16. Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.

# In[18]:


import re
text = 'The quick brown fox jumps over the lazy dog.'
literal_string = input("Enter your literal text: ")
match = re.search(literal_string, text)
a = match.start()
b = match.end()
print((literal_string), "is present between", a,"to",b )


# 17. Write a Python program to find the substrings within a string.

# In[19]:


import re
Sample_text= 'Python exercises, PHP exercises, C# exercises'
Pattern = 'exercises'
for match in re.findall(Pattern, Sample_text):
    print(Pattern)


# 18. Write a Python program to find the occurrence and position of the substrings within a string.

# In[20]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
substring = "exercises"
for match in re.finditer(substring, text):
    a = match.start()
    b = match.end()
    print((substring), "is present between", a,"to",b )


# 19. Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# In[21]:


import re
def convert(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2023-12-11"
print("Berofe convert formate is YYYY-MM-DD and Date: ",dt1)
print("After convert formate is DD-MM-YYYY and Date: ",convert(dt1))


# 20. Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.

# In[22]:


import re
text= input("Enter the floating number: ")
def find_dec(text):
    pattern = re.compile(r'\d+\.\d{1,2}')
    out= re.findall(pattern, text)
    return out
result= find_dec(text)
print("output: " ,result)


# 21. Write a Python program to separate and print the numbers and their position of a given string.

# In[23]:


import re
text= input("Enter your text: ")
for iteration in re.finditer("\d+", text):
    print("number: ", iteration.group())
    print("position:", iteration.start())


# 22. Write a regular expression in python program to extract maximum/largest numeric value from a string.

# In[24]:


import re
text= 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
result = re.findall('\d+', text)
print("largest numeric value from a string: ",max(result))


# 23. Create a function in python to insert spaces between words starting with capital letters.

# In[25]:


import re
def text():
    string = input("enter your text: ")
    pattern = r"\B(?=[A-Z])"
    new_text = re.sub(pattern, " ", string)
    print("After excute: ", new_text)
text()


# 24. Python regex to find sequences of one upper case letter followed by lower case letters.

# In[26]:


import re
text = input("Enter your text: ")
def match(text):
    pattern = '[A-Z]+[a-z]+$'
    if re.search(pattern, text):
        return True
    else:
        return False
match(text)


# 25. Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.

# In[27]:


import re
text = "Hello hello world world"
def remove(input):
    pattern = r'\b(\w+)(?:\W+\1\b)+'
    return re.sub(pattern, r'\1', input, flags=re.IGNORECASE)
print(remove(text))


# 26. Write a python program using RegEx to accept string ending with alphanumeric character.

# In[28]:


import re
string= input("Enter your text: ")
def check(string):
    pattern = r"[a-zA-Z]+[0-9]"
    match = re.search(pattern, string)
    if match:
        print("True")
    else:
        print("False")
check(string)


# 27. Write a python program using RegEx to extract the hashtags.

# In[29]:


import re
text= input("enter your text: ")
def extract(text):
    pattern = "#(\w+)"
    result = re.findall(pattern, text)
    for has in result:
        print(has)
extract(text)


# 28. Write a python program using RegEx to remove <U+..> like symbols Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.

# In[30]:


import re
text= input("Enter your text: ")
new_text = re.sub(r"<U\+\w{4}>", "", text)
print("new text: ", new_text)


# 29. Write a python program to extract dates from the text stored in the text file.

# In[31]:


import re
file = open("extract.txt",'r')
text = file.read()
match = re.findall(r'(\d+-\d+-\d+)',text)
print(match)


# 30. Create a function in python to remove all words from a string of length between 2 and 4. The use of the re.compile() method is mandatory.

# In[32]:


import re
string = input("Enter your text: ")
remove = re.compile(r'\W*\b\w{2,4}\b')
print("After removing: ", remove.sub("", string))

