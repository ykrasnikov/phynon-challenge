#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# IN dedication to Carlos's List Comprehensions and playing with dictionaries
# import os /csv , my hands are tied - no pandas
import os
import csv


# In[ ]:


# define path to file file_path="/Resources/budget_data.csv"
file_path=os.path.join("Resources","budget_data.csv")


# In[ ]:


# open file using csv open function, using csv reader to form csvreader object ....rows 
with open(file_path, 'r', encoding="utf-8") as csvfile:
    csvrow=csv.reader(csvfile, delimiter=",")
    header=(next(csvrow))
    # print(header) # debug print first row
    # create dictionary key =month , value =float of profits from csvreader object
    mydict = {r[0]:float(r[1]) for r in csvrow} 
    # print(mydict) #debug print dictionary


# In[ ]:


# creating reversed dictionary  key- change of profit from one month to another (original dates are sorted)
i_dict={}
for x,y in mydict.items():
    if x!=list(mydict.keys())[0]:  # skip first row in original as there is nothing to subtract
        i_dict[y-previous_month]=x
    previous_month=y               # little buffer for previous month value
print(i_dict)   


# In[ ]:


#if u decide not to reverse keys /values above , u can reverse here.... i_dict_r = dict(map(reversed, i_dict.items())) #i_dict_r = {value: key for key, value in i_dict.items()}
#print(i_dict_r)


# In[ ]:


# total months will be length of original dictionary keys , can just use 
total_month=len(mydict)
# print(total_month) #debug print


# In[ ]:


# finding max value for profit loss and corresponding date - create tuple from reversed change of profit dictionary
max_tuple=max(i_dict.items()) 
print(max_tuple) # debug print
#print(max(mydict.values())) # debug  check 


# In[ ]:


# same for min profit tuple
min_tuple=min(i_dict.items())
print(min_tuple)


# In[ ]:


#  suym of all profits - using sum function
total=sum(mydict.values())
formatted_total = "${:,.2f}".format(average_change)
print(formatted_total)


# In[ ]:


# average change in profit calculation - sum of keys divided by length
average_change=sum(i_dict.keys()) / len(i_dict)
formatted_ac = "${:,.2f}".format(average_change)
print(formatted_ac)


# In[ ]:




