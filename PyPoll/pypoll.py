#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import os /csv , my hands are tied - no pandas
import os
import csv


# In[2]:


# define path to file file_path="/Resources/election_data.csv"
file_path=os.path.join("Resources","election_data.csv")


# In[3]:


# open file using csv open function, using csv reader to form csvreader object ....rows 
with open(file_path, 'r', encoding="utf-8") as csvfile:
    csvrow=csv.reader(csvfile, delimiter=",")
    header=(next(csvrow))
    print(header) # debug print first row
    candidate_counter = {}
    for row in csvrow:
        if row[2] not in candidate_counter:
            candidate_counter[row[2]] = 1
        else:
            candidate_counter[row[2]] += 1 
    print(candidate_counter)


# In[4]:


total_votes=sum(candidate_counter.values())
print(total_votes)


# In[10]:


candidate_counter1={}
for key in candidate_counter:
    percent=(candidate_counter[key])/total_votes*100
    candidate_counter1[key]=[percent,candidate_counter[key]]
#print(candidate_counter)
print(candidate_counter1)


# In[8]:


max_key = max(candidate_counter1, key=candidate_counter1.get)
print(max_key)


# In[ ]:




