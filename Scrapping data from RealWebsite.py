#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[4]:


url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_India"


# In[5]:


page = requests.get(url)


# In[6]:


soup = BeautifulSoup(page.text,'html')


# In[7]:


print(soup)


# In[10]:


soup.find('table')


# In[26]:


soup.find_all('table',class_='wikitable sortable')[1]


# In[27]:


table = soup.find_all('table')[1]


# In[28]:


print(table)


# In[29]:


table.find_all('th')


# In[30]:


word_title


# In[31]:


word_table_title = [title.text.strip() for title in word_title]
print(word_table_title)


# In[32]:


df = pd.DataFrame(columns= word_table_title)
df


# In[34]:


column_data = table.find_all('tr')


# In[41]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    indivisual_row_data = [data.text.strip() for data in row_data]
    
    
    length = len(df)
    df.loc[length] = indivisual_row_data


# In[42]:


df


# In[44]:


df.to_csv(r'C:\Users\lenovo\Desktop\web_scrapping\my_scrap.csv', index=False)


# In[ ]:




