#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import os /csv , my hands are tied - no pandas
import os
import csv


# In[2]:


# define path to file file_path="/Resources/employee_data.csv"
file_path=os.path.join("Resources","employee_data.csv")


# In[3]:


states = {'Alaska': 'AK', 'Alabama': 'AL', 'Arkansas': 'AR', 'American Samoa': 'AS', 'Arizona': 'AZ', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'District of Columbia': 'DC', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Guam': 'GU', 'Hawaii': 'HI', 'Iowa': 'IA', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Massachusetts': 'MA', 'Maryland': 'MD', 'Maine': 'ME', 'Michigan': 'MI', 'Minnesota': 'MN', 'Missouri': 'MO', 'Northern Mariana Islands': 'MP', 'Mississippi': 'MS', 'Montana': 'MT', 'National': 'NA', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Nebraska': 'NE', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'Nevada': 'NV', 'New York': 'NY', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Puerto Rico': 'PR', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Virginia': 'VA', 'Virgin Islands': 'VI', 'Vermont': 'VT', 'Washington': 'WA', 'Wisconsin': 'WI', 'West Virginia': 'WV', 'Wyoming': 'WY'}
print(states)


# In[19]:


# open file using csv open function, using csv reader to form csvreader object ....rows 
with open(file_path) as csvfile:
    csv_reader=csv.reader(csvfile)
    header=(next(csv_reader))
    #row1=next(csv_reader)
    #print(len(list(csv_reader)))
    print(header) # debug print first row
    print(csv_reader)
    #print(row1)
    row_new=[]
    row_new_head=['Emp ID','First Name','Last Name','DOB','SSN','State']
    #row_new=[row1[0],row1[1].split()[0],row1[1].split()[1],f'{row1[2][5:7]}/{row1[2][-2:]}/{row1[2][:4]}',f'***-**-{row1[3][-4:]}',states[row1[4]]]
    
    #row_new=[[row1[0],row1[2]] for row1 in csv_reader]
    row_new=[[row1[0],row1[1].split()[0],row1[1].split()[1],f'{row1[2][5:7]}/{row1[2][-2:]}/{row1[2][:4]}',f'***-**-{row1[3][-4:]}',states[row1[4]]] for row1 in csv_reader]
    print(row_new)


# In[28]:


file_out_path=os.path.join("Resources","converted_employee_data.csv")
with open(file_out_path,'w') as csvfile:
    write = csv.writer(csvfile,lineterminator = '\n') 
    write.writerow(row_new_head)
    write.writerows(row_new)
   


# In[ ]:




