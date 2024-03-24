#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import json


# In[4]:


file_path = r'C:\Users\16147\Downloads\takeout-20240323T151031Z-001\Takeout\Location History (Timeline)\Semantic Location History\2023'


# In[32]:


months = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']


# In[93]:


all_data = []
for month in months:
    file_name = r'2023_'+ month +'.json'
    full_path = file_path + '\\' + file_name
    df = pd.read_json(full_path)

    for entry in df['timelineObjects']:
        if list(entry.keys())[0] == 'placeVisit': 
            try:    
                location = entry['placeVisit']['location']['address']
                time = entry['placeVisit']['duration']['startTimestamp']
                all_data.append((location,time))
            except:
                pass
    print(month + ' complete')


# In[98]:


final_df = pd.DataFrame(all_data,columns=['Address','Time'])


# In[104]:


final_df['Address']


# In[111]:


len(list(set([i[:10] for i in final_df['Time']])))


# In[123]:


final_df['in_us'] = [i[-3:]=='USA' for i in final_df['Address']]


# In[ ]:





# In[105]:


final_df.to_excel(r'C:\Users\16147\Downloads\test_data.xlsx')


# In[ ]:




